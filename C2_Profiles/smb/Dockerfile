FROM itsafeaturemythic/mythic_base_image:0.0.1

WORKDIR /Mythic/
COPY [".", "."]
RUN python3 -m pip install mythic-container==0.2.0rc4
CMD ["python3", "main.py"]