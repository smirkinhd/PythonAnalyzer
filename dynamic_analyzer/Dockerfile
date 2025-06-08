FROM python:3.13-rc-slim

RUN apt-get update && apt-get install -y \
    wget gnupg libglib2.0-0 libnss3 libgconf-2-4 libatk1.0-0 \
    libatk-bridge2.0-0 libx11-xcb1 libxcomposite1 libxdamage1 \
    libxrandr2 libasound2 libpangocairo-1.0-0 libcairo2 libpango-1.0-0 \
    libxshmfence1 libgbm1 libgtk-3-0 && \
    rm -rf /var/lib/apt/lists/*

RUN pip install playwright  \
    && playwright install --with-deps chromium  \
    && pip install aiohttp \
    && pip install aiofiles

WORKDIR /app
COPY ../../еу .

CMD ["python", "analyze_dynamic.py", "suspicious.html"]
