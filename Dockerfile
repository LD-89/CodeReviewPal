FROM python:3.12.3-slim-bullseye AS builder

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Rust 1.75+ for transformers safety
RUN apt-get update && apt-get install -y curl \
  && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
  && export PATH="$HOME/.cargo/bin:$PATH" \
  && cargo --version

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12.3-slim-bullseye

RUN apt-get update && apt-get install -y \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local/bin:$PATH

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]