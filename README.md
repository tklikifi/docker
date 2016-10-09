# Docker

This project shows an example of how to use docker and docker compose to setup
containers.

## Containers

### Redis Server

Redis server stores the data and acts as publishing channel.

### Frontend Server

Frontend server runs the simplest Flask application and publishes the visits
to the channel.

### Backend Server

Backend server records the visits to the frontend using the publishing
channel.
