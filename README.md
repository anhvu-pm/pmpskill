# PMP Skills

Helpful AI skills for PMP learners: review your practice results, understand competing answers, and take away concise principles for similar situations.

Kho kỹ năng AI dành cho người học PMP, bắt đầu với **`explain-pmp-questions`**: giúp bạn tự review câu hỏi đã làm, hiểu vì sao một phương án phù hợp hơn, và rút ra nguyên tắc ngắn gọn để áp dụng cho tình huống tương tự.

## Kỹ năng hiện có

| Skill | Khi nào dùng | Kết quả mong đợi |
|---|---|---|
| [explain-pmp-questions](skills/explain-pmp-questions/SKILL.md) | Bạn phân vân giữa các lựa chọn, chưa hiểu đáp án của bộ đề, hoặc muốn review câu làm sai | Giải thích tiếng Việt ngắn gọn; so sánh phương án; nêu `Principle:` khi có nguyên tắc phù hợp |

Skill hỗ trợ câu hỏi predictive, agile và hybrid; xem xét đúng yêu cầu `FIRST`, `NEXT`, `BEST`, `MOST` hoặc `SHOULD`. Đáp án được cung cấp vẫn cần được kiểm tra bằng dữ kiện của đề.

## Cài đặt

Bạn cần một công cụ AI hỗ trợ Agent Skills. Bản hiện tại gồm hướng dẫn và tài liệu tham khảo, không cần cài Python, Node.js hay API key riêng cho skill; quyền truy cập và chi phí sử dụng AI tùy công cụ của bạn.

### Codex: nhờ Skill Installer cài từ GitHub

Trong Codex, gửi yêu cầu:

```text
Use $skill-installer to install the skill from
https://github.com/anhvu-pm/pmpskill/tree/main/skills/explain-pmp-questions
```

Sau khi cài, tìm `explain-pmp-questions` trong danh sách skills. Nếu chưa xuất hiện, khởi động lại Codex. Xem [hướng dẫn skills chính thức của OpenAI](https://learn.chatgpt.com/docs/build-skills).

### Codex: cài thủ công

1. Tải ZIP từ GitHub: **Code → Download ZIP**, rồi giải nén; hoặc clone repo bằng Git.
2. Copy **toàn bộ thư mục** `skills/explain-pmp-questions` vào thư mục skills cá nhân:

   - Windows: `%USERPROFILE%\.agents\skills\explain-pmp-questions`
   - macOS / Linux: `~/.agents/skills/explain-pmp-questions`

3. Kiểm tra cấu trúc sau; giữ nguyên cả hai file trong `references/`:

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

Chỉ tải repo hoặc merge thay đổi trên GitHub chưa tự cài skill. Nếu bạn đã cài một bản copy, hãy lưu lại tùy chỉnh cá nhân trước khi thay bằng phiên bản mới; cập nhật repo không tự cập nhật bản copy đã cài.

### Công cụ AI khác

Dùng cơ chế cài Agent Skills của công cụ đó và giữ nguyên toàn bộ thư mục skill. Các bước cụ thể tùy công cụ; repo hiện chưa cung cấp gói plugin hoặc hướng dẫn cài đã kiểm chứng cho từng nền tảng.

Nếu công cụ chưa hỗ trợ cài skills, bạn có thể đính kèm `SKILL.md` và cả hai file tham khảo, rồi yêu cầu AI làm theo hướng dẫn. Đây là cách dùng thủ công; không tạo cài đặt lâu dài hoặc bảo đảm hành vi tương đương tích hợp skills.

## Bắt đầu với một câu hỏi

Copy mẫu sau và điền thông tin:

```text
Use $explain-pmp-questions to review this PMP practice question.

Câu hỏi: [nguyên văn câu hỏi]
A. [...]
B. [...]
C. [...]
D. [...]
[Thêm mọi lựa chọn còn lại nếu có.]

Đáp án bộ đề (nếu có): [...]
Lựa chọn của bạn (nếu có): [...]
Câu hỏi thêm (nếu có): [...]
```

Bạn sẽ thường nhận câu trả lời khoảng 80–180 từ: kết luận trước, 1–2 dữ kiện quyết định, so sánh với lựa chọn cạnh tranh và một nguyên tắc có phạm vi áp dụng rõ. Nếu đề mơ hồ, skill được hướng dẫn nói rõ điều đó. Không phải câu hỏi nào cũng cần tạo thêm một nguyên tắc mới.

Sau khi đọc, tự diễn đạt lại nguyên tắc và thử áp dụng vào câu tiếp theo. Mục tiêu là hiểu cách suy luận, thay vì chỉ nhớ chữ cái đáp án.

## Phạm vi và tình trạng hiện tại

- Đây là công cụ hỗ trợ học tập; người học cần đối chiếu lập luận với đề và tài liệu học của mình. AI vẫn có thể sai.
- Giọng trả lời mặc định là thân thiện, trực tiếp, ngắn gọn bằng tiếng Việt. Ví dụ hiệu chỉnh phong cách cá nhân của người duy trì được giữ riêng.
- Chưa có kết quả đánh giá thực thi được công bố; repo chưa đưa ra cam kết về độ chính xác hoặc kết quả thi.
- Tài liệu ECO đi kèm là bản tóm lược tham khảo cho July 2026; không phải bản dịch chính thức. Dự án độc lập, không phải sản phẩm của PMI.

## Góp ý và đóng góp

Mở [GitHub Issue](https://github.com/anhvu-pm/pmpskill/issues) khi bạn gặp lập luận chưa thuyết phục, hướng dẫn cài khó hiểu, hoặc có ý tưởng cho skill mới.

## License

[MIT License](LICENSE) © 2026 anhvu-pm.
