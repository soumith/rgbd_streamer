# Example to stream RGBD from one machine to another, including data-compression

Uses lossy compression for RGB and lossless for Depth

```bash
pip install -r requirements.txt
```

```bash
./name_server.sh &
python server.py
```

```bash
python client.py --ip [server_ip]
```
