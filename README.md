# mini-ems

A small energy management system used as a learning project.
Four services: a TimescaleDB database, a weather ingestion job,
a forecast API and a battery optimizer API.

Data source: Open-Meteo (temperature and solar radiation).
 
 Status: "update"
Usage: docker compose up (from week 2).
Workflow: one branch per change, merged into main through a pull request.
After a merge on GitHub: git switch main, then git pull.
