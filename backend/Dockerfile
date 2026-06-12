FROM python:3.12-slim

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install uv
RUN pip install uv

# Copy dependency files first (for caching)
COPY pyproject.toml uv.lock ./

# Install dependencies into container
RUN uv sync --frozen

# Copy project
COPY . .

# Expose port (Cloud Run uses 8080)
EXPOSE 8080

# Run server
CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8080"]