## Transformer là gì? 
**Transformer** là kiến trúc mạng nơ-ron được giới thiệu năm 2017 trong paper nổi tiếng **“Attention is All You Need”** (Vaswani et al.).  
Thay vì dùng RNN hay LSTM tuần tự chậm chạp, Transformer chỉ dùng cơ chế **Self-Attention** để xử lý toàn bộ câu cùng một lúc → nhanh hơn rất nhiều và đạt kết quả state-of-the-art trong hầu hết các tác vụ NLP.

Ngày nay, **hầu hết các mô hình ngôn ngữ lớn** (BERT, GPT, T5, LLaMA, PhoBERT, ViT5, Bloom…) đều dựa trên kiến trúc Transformer.

## Các thư viện & hàm chính đã dùng trong 2 ví dụ

| Thư viện / Hàm                          | Mô tả                                                                                 | Dùng ở ví dụ nào          |
|-----------------------------------------|---------------------------------------------------------------------------------------|---------------------------|
| `transformers` (Hugging Face)           | Thư viện mạnh nhất thế giới để tải & dùng >300.000 mô hình Transformer đã train sẵn   | Cả 2 ví dụ                |
| `pipeline()`                            | Hàm “một dòng code” của Hugging Face: tự động tải model + tokenizer + xử lý đầu vào/ra | Cả 2 ví dụ                |
| `torch` (PyTorch)                       | Backend tính toán của hầu hết các mô hình trong Hugging Face                           | Cả 2 (chạy ngầm)          |
| `sentencepiece`                         | Thư viện tokenizer cho các mô hình MarianMT (Helsinki-NLP)                            | Ví dụ 1                   |
| `accelerate`                            | Giúp pipeline chạy nhanh & ổn định hơn (bắt buộc từ transformers 4.30+)               | Cả 2 (khuyến khích)       |

→ Nhờ `pipeline()`, bạn **không cần viết code tokenizer, không cần quan tâm GPU/CPU**, chỉ cần 1-2 dòng là dùng được ngay.

## Giới thiệu ngắn 2 ví dụ đang có

### Ví dụ 1 – Dịch Anh ↔ Việt (Helsinki-NLP/opus-mt-en-vi)
- **Mô hình**: MarianMT – một phiên bản nhỏ gọn của Transformer chuyên dịch thuật  
- **Kích thước**: ~300 MB  
- **Đặc điểm**: Rất nhanh trên CPU, chất lượng dịch tốt với câu ngắn và trung bình  
- **Ứng dụng thực tế**: Dịch nhanh website, chat, tài liệu…

```python
translator("I love Vietnam")[0]["translation_text"]
# → Tôi yêu Việt Nam

```

### Ví dụ 2 – Điền từ bị che bằng PhoBERT (vinai/phobert-base)

- **Mô hình:** PhoBERT – phiên bản BERT được train riêng cho tiếng Việt (VinAI)
- **Kích thước:** ~500 MB
- **Đặc điểm:** Hiểu ngữ cảnh tiếng Việt cực tốt, dùng <mask> để dự đoán từ phù hợp
- **Ứng dụng thực tế:** Gợi ý từ, sửa lỗi chính tả, tạo trò chơi điền từ…

```
unmasker("Hà Nội là thủ đô <mask> Việt Nam")[:3]
# → 1. của   2. nước   3. và
```

### Danh sách thư viện cần tải


```bash
pip install --upgrade pip torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu transformers[torch] sentencepiece accelerate protobuf tqdm tokenizers datasets huggingface_hub safetensors underthesea vncorenlp
```