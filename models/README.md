# Model Artifacts

Model weights are not stored in this repository.

Use a local model path at runtime:

```powershell
python -m src.pipeline --model path\to\model.pt --source 0 --show
```

For NVIDIA Jetson, use a PyTorch/runtime build compatible with the target JetPack and CUDA version.

Do not commit proprietary weights, private training data, credentials, or employer-owned model artifacts.
