# Install uv
FROM python:3.13-slim-bookworm AS base
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN apt-get update && apt-get install -y --no-install-recommends \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

FROM base AS build
WORKDIR /app
# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-editable
# Copy the project into the intermediate image
ADD . /app
# Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-editable

FROM base AS runtime
# Copy the environment, but not the source code
COPY --from=build --chown=app:app /app /app
WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"
# Copy supervisord config file
RUN cp /app/server/supervisor.conf /etc/supervisor/conf.d/supervisord.conf
RUN touch /var/run/supervisor.sock && chmod 777 /var/run/supervisor.sock