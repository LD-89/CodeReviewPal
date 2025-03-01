# Stage 1: Build environment
FROM python:3.12.3-slim-bullseye AS builder

# Install build dependencies with cleanup
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Rust with proper PATH persistence
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
    && export PATH="/root/.cargo/bin:${PATH}" \
    && cargo --version

WORKDIR /app
COPY requirements.txt .

# Install Python dependencies to user directory
RUN pip install --no-cache-dir --user -r requirements.txt

# ----------------------------
# Stage 2: Runtime environment
FROM python:3.12.3-slim-bullseye

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# Copy dependencies from builder
COPY --from=builder --chown=appuser:appuser /root/.local /home/appuser/.local
COPY --chown=appuser:appuser . .

# Set environment variables
ENV PATH="/home/appuser/.local/bin:${PATH}" \
    PYTHONPATH="/home/appuser/.local/lib/python3.12/site-packages:${PYTHONPATH}"

# Switch to non-root user
USER appuser

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]