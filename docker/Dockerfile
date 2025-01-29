FROM python:3.12-bullseye

# install uv to run stdio clients (uvx)
RUN pip install --no-cache-dir uv

# install npx to run stdio clients (npx)
RUN apt-get update && apt-get install -y --no-install-recommends curl gettext
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
RUN apt-get install -y --no-install-recommends nodejs
    
COPY --from=requirements pyproject.toml pyproject.toml


## FOR GHCR BUILD PIPELINE
COPY --from=requirements README.md README.md
COPY --from=requirements mcp_bridge/__init__.py mcp_bridge/__init__.py
COPY --from=requirements mcp_bridge mcp_bridge

RUN uv sync


EXPOSE 8000

COPY config.json.template config.json.template
COPY entrypoint.sh entrypoint.sh

ENTRYPOINT ["bash", "entrypoint.sh"]
