FROM python:3.11-alpine   # minimal footprint :contentReference[oaicite:5]{index=5}
WORKDIR /usr/src/app

# install build deps, then remove to keep image small
RUN apk add --no-cache gcc musl-dev \
 && pip install --upgrade pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./

# healthcheck to ensure app responsiveness
HEALTHCHECK --interval=30s --timeout=5s \
  CMD wget --spider http://localhost:5000/health || exit 1

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
