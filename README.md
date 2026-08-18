# Vision Board — Azure Cloud Infrastructure, CI/CD & Monitoring

A small Python Flask Vision Board application that will be progressively deployed and operated as an Azure DevOps project.

## Current application features

- Add vision/goal cards
- Add descriptions and image URLs
- Mark goals as completed
- Delete goals
- SQLite persistence
- Health endpoint at `/health`
- Automated tests
- Docker support
- GitHub Actions CI

## Planned DevOps implementation

1. Containerize with Docker
2. Deploy to an Azure Linux VM
3. Configure GitHub Actions CI/CD
4. Configure Azure Monitor and VM Insights
5. Configure Azure RBAC
6. Explore VM Scale Sets
7. Add Python/Bash operational automation

## Local setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000

## Docker

```bash
docker build -t vision-board .
docker run -d --name vision-board -p 5000:5000 vision-board
```

Open http://localhost:5000

## Health check

Open http://localhost:5000/health
