# Beamline integration test

This is a github action repository for testing a conda environment from an
artifact against a given beamline ipython profile. It uses blackhole IOC to
attempt to start the beamline ipython profile.

## Beamline-specific configurations
Note that beamline-specific preconditioning actions can be added to `special_config.py`.