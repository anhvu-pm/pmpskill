# PMP Skills

Helpful AI skills for PMP learners: review your practice results, understand competing answers, and take away concise principles for similar situations.

Kho kỹ năng AI dành cho người học PMP, bắt đầu với **`explain-pmp-questions`**: giúp bạn tự review câu hỏi đã làm, hiểu vì sao một phương án phù hợp hơn, và rút ra nguyên tắc ngắn gọn để áp dụng cho tình huống tương tự.

## Kỹ năng hiện có

| Skill | Khi nào dùng | Kết quả mong đợi |
|---|---|---|
| [explain-pmp-questions](skills/explain-pmp-questions/SKILL.md) | Bạn phân vân giữa các lựa chọn, chưa hiểu đáp án của bộ đề, hoặc muốn review câu làm sai | Giải thích tiếng Việt ngắn gọn; so sánh phương án; nêu `Principle:` khi có nguyên tắc phù hợp |

Skill hỗ trợ câu hỏi predictive, agile và hybrid. Đáp án được cung cấp vẫn cần được kiểm tra bằng dữ kiện của đề.

## Sử dụng trong ChatGPT

### Dùng ngay để review câu hỏi

1. Tải repo: **Code → Download ZIP**, rồi giải nén.
2. Trong ChatGPT, đính kèm **cả ba file** từ `skills/explain-pmp-questions/`:
   - `SKILL.md`
   - `references/pmp-exam-content-outline.md`
   - `references/pmp-principles.md`
3. Gửi yêu cầu sau cùng ảnh hoặc nội dung câu hỏi:

```text
Hãy đọc SKILL.md và hai tài liệu tham khảo đính kèm.
Làm theo workflow explain-pmp-questions để review câu hỏi PMP dưới đây.
[Ảnh hoặc nguyên văn câu hỏi và các lựa chọn]
[Lựa chọn của tôi và điều tôi còn thắc mắc, nếu có]
```

Đây là cách dùng thủ công trong cuộc trò chuyện, **chưa phải cài skill vào tài khoản**. Khi mở cuộc trò chuyện khác, cần cung cấp lại các file nếu ChatGPT chưa có quyền truy cập chúng. Không chỉ gửi riêng SKILL.md vì workflow cần cả hai tài liệu tham khảo.

### Cài skill và dùng lại

Theo [tài liệu OpenAI](https://learn.chatgpt.com/docs/build-skills), skill độc lập được hỗ trợ trên ChatGPT desktop; skill đóng gói trong plugin có thể dùng trên ChatGPT web, desktop và mobile. Trên desktop, mở **Skills** để kiểm tra các skill có sẵn. Nếu đã cài thành công, gõ `@` và chọn skill khi review câu hỏi.

**Tình trạng repo:** hiện cung cấp mã nguồn skill, chưa có plugin cài đặt để phân phối cho học viên. Chưa kiểm chứng cài đặt đồng bộ vào tài khoản ChatGPT từ repo này; việc gửi link GitHub hoặc tải file lên chat không tự xác nhận skill đã được cài. Chỉ coi là hoàn tất khi skill xuất hiện trong danh sách và dùng được ở cuộc trò chuyện mới.

Nếu muốn phân phối một cách cài dùng được trên web/mobile, bước tiếp theo là đóng gói và kiểm chứng plugin. Trong lúc đó, dùng cách đính kèm ba file ở trên để thử với câu hỏi thực tế.

## Cài đặt bổ sung cho Codex

Dành cho người dùng Codex có hỗ trợ cài Agent Skills. Đây là cài đặt cho môi trường Codex, không xác nhận cài đặt đồng bộ cho ChatGPT web/mobile.

### Nhờ Skill Installer cài từ GitHub

Trong Codex, gửi yêu cầu:

```text
Use $skill-installer to install the skill from
https://github.com/anhvu-pm/pmpskill/tree/main/skills/explain-pmp-questions
```

Sau khi cài, tìm `explain-pmp-questions` trong danh sách skills và thử trong cuộc trò chuyện mới. Nếu chưa xuất hiện, khởi động lại Codex.

### Cài thủ công cho Codex

1. Tải ZIP từ GitHub: **Code → Download ZIP**, rồi giải nén; hoặc clone repo bằng Git.
2. Copy **toàn bộ thư mục** `skills/explain-pmp-questions` vào thư mục skills cá nhân:
   - Windows: `%USERPROFILE%\.agents\skills\explain-pmp-questions`
   - macOS / Linux: `~/.agents/skills/explain-pmp-questions`
3. Giữ nguyên cấu trúc:

```text
explain-pmp-questions/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── pmp-exam-content-outline.md
    └── pmp-principles.md
```

4. Mở cuộc trò chuyện mới, chọn skill hoặc gọi `$explain-pmp-questions`. Nếu skill chưa hiện, khởi động lại Codex.

### Công cụ AI khác

Dùng cơ chế cài Agent Skills của công cụ đó và giữ nguyên toàn bộ thư mục skill. Các bước cụ thể tùy công cụ; repo chưa cung cấp hướng dẫn cài đã kiểm chứng cho từng nền tảng.

## Bắt đầu với một câu hỏi

Trong ChatGPT, dùng mẫu này sau khi đính kèm đủ ba file hoặc chọn skill đã cài bằng `@`. Trong Codex, có thể gọi `$explain-pmp-questions`.

```text
Hãy dùng workflow explain-pmp-questions để review câu hỏi PMP này.

Có thể đính kèm ảnh màn hình hoặc cung cấp thông tin:
[Nguyên văn câu hỏi]
[Đáp án (nếu có)]
[Lựa chọn của bạn & câu hỏi thêm (nếu có)]
```

Bạn sẽ thường nhận câu trả lời khoảng 80–180 từ: kết luận trước, 1–2 dữ kiện quyết định, so sánh với lựa chọn cạnh tranh và một nguyên tắc hỗ trợ việc suy luận. Nếu đề mơ hồ, skill được hướng dẫn nói rõ điều đó. Không phải câu hỏi nào cũng có nguyên tắc để takeaway.

Sau khi đọc, tự diễn đạt lại nguyên tắc và thử áp dụng vào câu tiếp theo. Mục tiêu là hiểu cách suy luận, thay vì chỉ nhớ keywords đáp án.

## Phạm vi và tình trạng hiện tại

- Đây là công cụ hỗ trợ học tập; người học cần đối chiếu lập luận với đề và tài liệu học của mình. AI vẫn có thể sai.
- Giọng trả lời mặc định là thân thiện, trực tiếp, ngắn gọn bằng tiếng Việt. Ví dụ hiệu chỉnh phong cách cá nhân của người duy trì được giữ riêng.
- Chưa có kết quả đánh giá thực thi được công bố; repo chưa đưa ra cam kết về độ chính xác hoặc kết quả thi.
- Dự án độc lập, không phải sản phẩm của PMI.

## Góp ý và đóng góp

Mở [GitHub Issue](https://github.com/anhvu-pm/pmpskill/issues) khi bạn gặp lập luận chưa thuyết phục, hướng dẫn cài khó hiểu, hoặc có ý tưởng cho skill mới.

## License

[MIT License](LICENSE) © 2026 anhvu-pm.
