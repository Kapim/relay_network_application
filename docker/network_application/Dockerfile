FROM ros:humble

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Prague
ENV LANG C.UTF-8

RUN apt-get update \
    && apt-get install -y python3-pip ros-humble-rosbridge-library ros-humble-cv-bridge ros-humble-sensor-msgs-py ros-humble-action-msgs ros-humble-actionlib-msgs ros-humble-cartographer-ros-msgs ros-humble-diagnostic-msgs ros-humble-geometry-msgs ros-humble-map-msgs ros-humble-nav-msgs ros-humble-nav2-msgs ros-humble-octomap-msgs ros-humble-tf2-geometry-msgs ros-humble-tf2-msgs ros-humble-trajectory-msgs ros-humble-visualization-msgs

RUN python3 -m pip install era_5g_relay_network_application

COPY docker/network_application/start.sh /root/start.sh
COPY docker/network_application/DEFAULT_FASTRTPS_PROFILES.xml /root/DEFAULT_FASTRTPS_PROFILES.xml

ENV FASTRTPS_DEFAULT_PROFILES_FILE=/root/DEFAULT_FASTRTPS_PROFILES.xml

RUN chmod +x /root/start.sh
ENTRYPOINT [ "/root/start.sh" ] 