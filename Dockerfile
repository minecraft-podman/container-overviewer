FROM xonsh/xonsh AS build
RUN xpip install wheel numpy pillow
RUN git clone https://github.com/astronouth7303/Minecraft-Overviewer.git -b update-setupy /tmp/overviewer
COPY build.xsh /tmp/overviewer
WORKDIR /tmp/overviewer
RUN xonsh build.xsh

FROM python:3-slim
ARG mcversion
COPY --from=build /tmp/overviewer/dist/*.whl /tmp
RUN pip install /tmp/*.whl
ARG version=latest
ADD https://overviewer.org/textures/${version}  ~/.minecraft/versions/${version}/${version}.jar

VOLUME ["/mc/snapshot", "/srv/overviewer"]
CMD ["overviewer.py", "/mc/snapshot", "/srv/overviewer"]
