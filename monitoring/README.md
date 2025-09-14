# Monitoring Stack

This directory contains the configuration and setup for a Docker-based monitoring stack. It includes Prometheus for metrics collection, Alertmanager for alerting, and related configuration files. The stack is orchestrated using Docker Compose.

## Directory Structure

- `docker-compose.yml` - Docker Compose file to set up and run the monitoring stack.
- `AlertManager/`
  - `alertmanager.yml` - Main configuration file for Alertmanager.
- `prometheus/`
  - `prometheus.yml` - Main configuration file for Prometheus.
  - `alert_rules.yml` - Custom alerting rules for Prometheus.

## Usage

1. **Start the Monitoring Stack**
   
   Open a terminal in this directory and run:
   
   ```powershell
   docker-compose up -d
   ```

2. **Prometheus**
   - Access Prometheus at: [http://localhost:9090](http://localhost:9090)
   - Configuration: `prometheus/prometheus.yml`
   - Alert rules: `prometheus/alert_rules.yml`

3. **Alertmanager**
   - Access Alertmanager at: [http://localhost:9093](http://localhost:9093)
   - Configuration: `AlertManager/alertmanager.yml`

## Customization

- Edit `prometheus/prometheus.yml` to add scrape targets or change Prometheus settings.
- Edit `prometheus/alert_rules.yml` to define custom alerting rules.
- Edit `AlertManager/alertmanager.yml` to configure alert receivers and routing.

## Notes

- Ensure Docker and Docker Compose are installed on your system.

## References
- [Prometheus Documentation](https://prometheus.io/docs/)
- [Alertmanager Documentation](https://prometheus.io/docs/alerting/latest/alertmanager/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
