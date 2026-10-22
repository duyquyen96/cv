#!/usr/bin/env python3
"""Regenerate alternate CV styles with identical content to nguyen-duy-quyen-cv.html."""

from pathlib import Path

DIR = Path(__file__).parent

# ── Shared content (must match nguyen-duy-quyen-cv.html) ──────────────────────

NAME = "Nguyễn Duy Quyền"
ROLE = "Python Fullstack Developer · Tech Lead RnD"
ROLE_BR = "Python Fullstack Developer<br>Tech Lead RnD"
CONTACT = [
    ("Email", "duyquyencnt55@gmail.com", "mailto:duyquyencnt55@gmail.com", "email"),
    ("Điện thoại", "0963 108 848", "tel:0963108848", "phone"),
    ("Địa chỉ", "An Biên, Hải Phòng, Việt Nam", None, "location"),
    ("GitHub", "github.com/duyquyen96", "https://github.com/duyquyen96", "github"),
]
SKILLS_ODOO = ["Python", "JavaScript (ES6+)", "Odoo", "OWL", "React", "React Native", "Flutter", "PostgreSQL", "MySQL", "RESTful API", "XML-RPC", "JSON-RPC"]
SKILLS_AI = ["Git", "Docker", "Linux (Ubuntu)", "Claude AI", "Cursor", "VS Code"]
SKILLS_SOFT = ["Agile", "Scrum", "Phân tích nghiệp vụ", "BRD / SRS", "Functional Specification", "GAP Analysis", "Automation Testing"]
EDU = {
    "degree": "Kỹ sư Công nghệ Thông tin",
    "school": "Trường Đại học Hàng hải Việt Nam",
    "meta": "2014 - 2019",
}
SUMMARY = (
    'Lập trình viên Python Fullstack với <strong>hơn 7 năm kinh nghiệm phát triển phần mềm</strong> '
    'và <strong>hơn 3 năm chuyên sâu về hệ thống ERP</strong>. Có kinh nghiệm phát triển, tùy chỉnh module, '
    'nâng cấp hệ thống, tối ưu hiệu năng và tích hợp các nền tảng bên ngoài. '
    'Đã tham gia nhiều dự án chuyển đổi số quy mô lớn cho doanh nghiệp.'
)
JOBS = [
    {
        "title": "Kỹ sư lập trình · Tech Lead RnD",
        "period": "06/2026 - Hiện tại",
        "company": "Tập đoàn Bưu chính Viễn thông Việt Nam (VNPT)",
        "bullets": [
            "Đảm nhiệm chức vụ Tech Lead tại bộ phận Nghiên cứu và Phát triển (RnD).",
            "Tham gia phát triển VNPT LAEP Platform, website laegrid.vn và dự án Sàn việc làm của Bộ Nội vụ.",
        ],
    },
    {
        "title": "Product Software Developer",
        "period": "11/2022",
        "company": "Công ty Cổ phần Công nghệ Viindoo",
        "bullets": [
            "Phát triển và cải tiến hệ thống Viindoo ERP trên nền tảng Odoo, bao gồm ứng dụng di động và Progressive Web Apps (PWA).",
            "Tham gia Sprint Planning, Daily Scrum, Sprint Review và Retrospective trong môi trường Agile/Scrum.",
            "Phân tích yêu cầu nghiệp vụ, thiết kế giải pháp và triển khai tính năng mới; phối hợp với BA, Tester và các bên liên quan để đảm bảo chất lượng sản phẩm.",
            "Tối ưu hiệu năng, xử lý sự cố, nâng cấp Odoo từ phiên bản 13 trở lên và chuyển đổi dữ liệu.",
            "Đóng góp cho các dự án mã nguồn mở OCA và Odoo.",
        ],
    },
    {
        "title": "Mobile Developer",
        "period": "07/2020 - 11/2022",
        "company": "365 Technology Applications Limited Company",
        "bullets": [
            "Thiết kế và phát triển ứng dụng di động bằng React Native và Flutter.",
            "Phát hành ứng dụng lên Apple App Store và Google Play; xử lý các vấn đề bị từ chối khi xét duyệt.",
            "Tham gia các ứng dụng Landchat, Seaman Shop Vietnam, Thiền Hiện Đại Me-medi, Hải Sản Biển Đông, Minato và CTV Shop PT.",
        ],
    },
    {
        "title": "Backend Developer",
        "period": "06/2018 - 07/2020",
        "company": "PE Technology Solution Joint Stock Company",
        "bullets": [
            "Phân tích yêu cầu nghiệp vụ cho quy trình khai thác hàng hóa và thông quan.",
            "Phân tích, thiết kế hệ thống quản lý giao nhận vận tải (Freight Forwarding Management System) bằng PHP, HTML, CSS, jQuery và MySQL.",
        ],
    },
]
AI_BULLETS = [
    'Hiểu các lỗ hổng bảo mật phổ biến: RCE, SQL Injection, XSS và các nguyên tắc bảo mật ứng dụng web.',
    'Ứng dụng AI để giải quyết các tác vụ trong công việc.',
    'Soạn tài liệu BRD, SRS, Functional Specification và GAP Analysis.',
    'Thiết kế test case và thực hiện kiểm thử tự động.',
]
PROJECT_NOTE = "Các nền tảng, dự án ứng dụng UAV / AI, chuyển đổi số, ERP và ứng dụng di động tiêu biểu."
PROJECTS = [
    ("VNPT LAEP Platform", " · VNPT · Vai trò: Tech Lead · Nền tảng dịch vụ kinh tế tầm thấp", [
        "Phát triển nền tảng dịch vụ kinh tế tầm thấp, ứng dụng UAV và AI để giải quyết các bài toán thực tiễn.",
    ]),
    ("Website dịch vụ kinh tế tầm thấp VNPT", " · VNPT · Vai trò: Tech Lead", [
        'Phát triển website <a href="https://laegrid.vn/">laegrid.vn</a> giới thiệu dịch vụ kinh tế tầm thấp của VNPT.',
    ]),
    ("Sàn việc làm của Bộ Nội vụ", " · Bộ Nội vụ · Vai trò: Tech Lead", [
        "Tham gia phát triển dự án Sàn việc làm của Bộ Nội vụ.",
    ]),
    ("Nâng cấp và tích hợp Viindoo ERP", " · Viindoo · Odoo 13+", [
        "Nâng cấp hệ thống qua nhiều phiên bản Odoo; phát triển thương mại điện tử, tích hợp chấm công, báo cáo hợp nhất và báo cáo kho.",
        "Tích hợp Facebook, LinkedIn và tỷ giá ngân hàng ACB; chuyển đổi dữ liệu hành chính sau sắp xếp đơn vị hành chính.",
    ]),
    ("Chuyển đổi số doanh nghiệp", " · Weldcom / Thủy điện Hòa Bình / Xuất nhập khẩu Cao Bằng", [
        "Tham gia các dự án chuyển đổi số; tối ưu hệ thống báo cáo cho chuỗi bán lẻ tại Xuất nhập khẩu Cao Bằng.",
    ]),
    ("Ứng dụng di động tích hợp Odoo", " · Flutter / React Native / PWA", [
        "Phát triển và bảo trì ứng dụng Thủy điện Hòa Bình, ứng dụng nội bộ Viindoo và ứng dụng mua sắm Zulo.",
    ]),
    ("Ứng dụng di động tại 365 Technology", " · React Native / Flutter", [
        "Landchat (bất động sản), Seaman Shop Vietnam (thương mại điện tử), Thiền Hiện Đại Me-medi (nhạc thiền).",
        "Hải Sản Biển Đông (bán hàng), Minato (học tiếng Nhật trực tuyến), CTV Shop PT (bán hàng affiliate).",
    ]),
]
MORE_TAGS = ["UAV / AI", "Kinh tế tầm thấp", "Nền tảng số", "ERP", "E-commerce", "Mobile / PWA", "Tích hợp hệ thống", "Chuyển đổi dữ liệu", "Mã nguồn mở"]
MORE_TEXT = ""
MORE_CTA = ""
PERSONAL = '<section class="main-section"><h2>Thông tin cá nhân &amp; Chứng chỉ</h2><p class="summary">Ngày sinh: 07/10/1996 · Giới tính: Nam<br>MOS 2010 (2017) · TOEIC 495 (2019)</p></section>'

ICONS = {
    "email": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 7l10 7 10-7"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12 12 0 0 0 8.09 9.91"/></svg>',
    "location": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "github": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>',
}


def bullets_html(items, indent=10):
    lis = "\n".join(f'{" "*indent}<li>{b}</li>' for b in items)
    return f'{" "*indent}<ul>\n{lis}\n{" "*indent}</ul>'


def jobs_html(indent=8):
    parts = []
    for j in JOBS:
        parts.append(f'''{" "*indent}<div class="job">
{" "*indent}  <div class="job-header">
{" "*indent}    <span class="job-title">{j["title"]}</span>
{" "*indent}    <span class="job-period">{j["period"]}</span>
{" "*indent}  </div>
{" "*indent}  <div class="job-company">{j["company"]}</div>
{bullets_html(j["bullets"], indent + 2)}
{" "*indent}</div>''')
    return "\n".join(parts)


def projects_html(indent=8):
    parts = []
    for title, meta, blts in PROJECTS:
        parts.append(f'''{" "*indent}<div class="project">
{" "*indent}  <div class="project-header">{title}<span class="project-meta">{meta}</span></div>
{bullets_html(blts, indent + 2)}
{" "*indent}</div>''')
    return "\n".join(parts)


def main_content(indent=6):
    return f'''{" "*indent}<section class="main-section">
{" "*indent}  <h2>Tóm tắt</h2>
{" "*indent}  <p class="summary">{SUMMARY}</p>
{PERSONAL}
{" "*indent}</section>

{" "*indent}<section class="main-section">
{" "*indent}  <h2>Kinh nghiệm làm việc</h2>
{jobs_html(indent + 2)}
{" "*indent}</section>

{" "*indent}<section class="main-section ai-section">
{" "*indent}  <h2>Kỹ năng bổ sung</h2>
{" "*indent}  <div class="job">
{bullets_html(AI_BULLETS, indent + 4)}
{" "*indent}  </div>
{" "*indent}</section>

{" "*indent}<section class="main-section">
{" "*indent}  <h2>Dự án tiêu biểu</h2>
{" "*indent}  <p class="section-note">{PROJECT_NOTE}</p>
{projects_html(indent + 2)}
{" "*indent}  <div class="projects-more">
{" "*indent}    <span class="projects-more-label">Các dự án &amp; hạng mục khác đã tham gia:</span>
{" "*indent}    <div class="projects-tags">{"".join(f"<span>{t}</span>" for t in MORE_TAGS)}</div>
{" "*indent}    {MORE_TEXT}
{" "*indent}    <span class="projects-cta">{MORE_CTA}</span>
{" "*indent}  </div>
{" "*indent}</section>'''


def sidebar_skills(indent=6):
    def tags(items):
        return "".join(f'<span class="skill-tag">{s}</span>' for s in items)
    return f'''{" "*indent}<div class="sidebar-section"><h2>Lập trình &amp; ERP</h2><div class="skill-tags">{tags(SKILLS_ODOO)}</div></div>
{" "*indent}<div class="sidebar-section"><h2>Công cụ &amp; AI</h2><div class="skill-tags">{tags(SKILLS_AI)}</div></div>
{" "*indent}<div class="sidebar-section"><h2>Quy trình &amp; Tài liệu</h2><div class="skill-tags">{tags(SKILLS_SOFT)}</div></div>
{" "*indent}<div class="sidebar-section"><h2>Học vấn</h2>
{" "*indent}  <div class="edu-degree">{EDU["degree"]}</div>
{" "*indent}  <div class="edu-school">{EDU["school"]}</div>
{" "*indent}  <div class="edu-meta">{EDU["meta"]}</div>
{" "*indent}</div>'''


def contact_sidebar(indent=8):
    rows = []
    for label, text, href, icon in CONTACT:
        val = f'<a href="{href}">{text}</a>' if href else text
        rows.append(f'''{" "*indent}<li>
{" "*indent}  <span class="contact-icon" aria-hidden="true">{ICONS[icon]}</span>
{" "*indent}  <div class="contact-body"><span class="contact-label">{label}</span>{val}</div>
{" "*indent}</li>''')
    return "\n".join(rows)


SHARED_MAIN_CSS = '''
    .main-section { margin-bottom: 18px; }
    .main-section:last-child { margin-bottom: 0; }
    .section-note { font-size: 8.5pt; color: var(--muted); font-style: italic; margin-bottom: 12px; line-height: 1.4; }
    .summary { font-size: 10pt; text-align: justify; line-height: 1.5; }
    .summary strong { font-weight: 700; }
    .job { margin-bottom: 14px; break-inside: avoid; page-break-inside: avoid; }
    .job:last-child { margin-bottom: 0; }
    .job-header { display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 4px 12px; margin-bottom: 2px; }
    .job-title { font-weight: 700; font-size: 10.5pt; }
    .job-period { font-size: 9pt; color: var(--muted); white-space: nowrap; font-weight: 600; }
    .job-company { font-size: 9.5pt; color: var(--muted); font-style: italic; margin-bottom: 6px; }
    .job ul { padding-left: 16px; }
    .job li { font-size: 9.5pt; margin-bottom: 3px; line-height: 1.4; }
    .project { margin-bottom: 11px; break-inside: avoid; page-break-inside: avoid; }
    .project-header { font-size: 9.5pt; font-weight: 700; margin-bottom: 4px; line-height: 1.35; }
    .project-meta { font-weight: 400; color: var(--muted); font-size: 9pt; }
    .project ul { padding-left: 14px; }
    .project li { font-size: 9.5pt; margin-bottom: 2px; line-height: 1.4; }
    .projects-more { margin-top: 12px; font-size: 9pt; line-height: 1.45; color: var(--muted); }
    .projects-more-label { color: var(--text); font-weight: 400; }
    .projects-tags { display: flex; flex-wrap: wrap; gap: 4px; margin: 6px 0 8px; }
    .projects-tags span { font-size: 8pt; background: #fff; border: 1px solid var(--border); border-radius: 3px; padding: 2px 6px; color: var(--text); }
    .projects-cta { display: block; font-size: 8.5pt; color: var(--muted); font-style: italic; }
    .ai-section .job li strong { font-weight: 700; }
    @media print {
      body { background: #fff; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
      .cv, .cv-page { margin: 0; box-shadow: none; max-width: none; width: 100%; border-radius: 0; overflow: visible; }
      .profile, .chips, .projects-more, .summary { break-inside: avoid; page-break-inside: avoid; }
      .main-section > h2, .main h2 { break-after: avoid; page-break-after: avoid; }
      @page { size: A4; margin: 0; }
    }
'''


MOBILE_STACK_CSS = '''
      body { background: #fff; font-size: 10pt; overflow-x: hidden; }
      .cv-page, .cv {
        margin: 0;
        width: 100%;
        max-width: 100%;
        min-width: 0;
        min-height: auto;
        box-shadow: none;
        border-radius: 0;
        display: block !important;
        grid-template-columns: none !important;
      }
      .sidebar, aside.sidebar {
        width: 100%;
        border-right: none !important;
        border-left: none !important;
        border-bottom: 2px solid var(--navy, var(--accent, var(--coral, var(--ocean, #1e3a5f))));
        padding: 20px 16px;
      }
      .main, main.main { padding: 20px 16px; width: 100%; }
      .body, .layout { display: block !important; }
      .body .sidebar, .body .main,
      .layout .sidebar, .layout .main {
        border-right: none !important;
        border-left: none !important;
      }
      .top, .banner, .head {
        display: block !important;
        grid-template-columns: none !important;
        text-align: center;
        padding: 20px 16px;
      }
      .top .avatar, .banner .avatar, .head .avatar {
        margin-left: auto;
        margin-right: auto;
      }
      .top-left { flex-direction: column; align-items: center; text-align: center; }
      .contact-row, .contact, .profile .contact { justify-content: center; }
      .cols, .skills-grid, .skills-row { grid-template-columns: 1fr !important; }
      .profile {
        flex-direction: column;
        align-items: center;
        text-align: center;
      }
      .chips { flex-direction: column; gap: 12px; }
      .chip-group p { max-width: none; }
      .wrap { padding: 16px; }
      .cv { padding-left: 0; padding-right: 0; }
      .job-header { flex-direction: column; align-items: flex-start; gap: 2px; }
      .job-period { white-space: normal; }
      .contact-list a, .contact-body { overflow-wrap: anywhere; word-break: normal; }
      .wave, .accent-bar { display: block; }
'''

def _embed_css(mobile_css):
    import re

    lines = []
    single_line = re.compile(r"^(.+?)\s*\{(.+)\}\s*$")
    for line in mobile_css.split("\n"):
        stripped = line.strip()
        if not stripped:
            lines.append(line)
            continue
        indent = line[: len(line) - len(line.lstrip())]
        match = single_line.match(stripped)
        if match and "{" not in match.group(1):
            parts = [p.strip() for p in match.group(1).split(",")]
            prefixed = ", ".join(
                p if p.startswith("html.cv-embed") else f"html.cv-embed {p}"
                for p in parts
            )
            lines.append(f"{indent}{prefixed} {{ {match.group(2).strip()} }}")
            continue
        if stripped.endswith("{"):
            selector = stripped[:-1].strip()
            parts = [p.strip() for p in selector.split(",")]
            prefixed = ", ".join(
                p if p.startswith("html.cv-embed") else f"html.cv-embed {p}"
                for p in parts
            )
            lines.append(f"{indent}{prefixed} {{")
        else:
            lines.append(line)
    return "\n".join(lines)


EMBED_STACK_CSS = _embed_css(MOBILE_STACK_CSS)

RESPONSIVE_CSS = f'''
    html {{ -webkit-text-size-adjust: 100%; }}
    @media screen {{
      body {{
        container-type: inline-size;
        container-name: cv-root;
        min-width: 0;
        overflow-x: hidden;
      }}
      .cv-page, .cv {{ width: 100%; min-width: 0; }}
      @container cv-root (max-width: 600px) {{
{MOBILE_STACK_CSS}
      }}
    }}
    @media screen and (max-width: 600px) {{
{MOBILE_STACK_CSS}
    }}
{EMBED_STACK_CSS}
'''

EMBED_SCRIPT = '''
  <script>
    (function () {
      if (new URLSearchParams(location.search).get("embed") === "1") {
        document.documentElement.classList.add("cv-embed");
      }
    })();
  </script>
'''


def wrap(title, css, body):
    return f'''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <style>
{css.rstrip()}{RESPONSIVE_CSS}
    .job-company a, .project a {{ color: inherit; text-decoration: underline; text-underline-offset: 2px; }}
  </style>
</head>
<body>
{body}
{EMBED_SCRIPT}
</body>
</html>
'''


def gen_modern():
    css = '''
    :root { --accent: #0d9488; --accent-dark: #0f766e; --text: #1e293b; --muted: #64748b; --border: #e2e8f0; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: system-ui, sans-serif; font-size: 10.5pt; line-height: 1.45; color: var(--text); background: #f1f5f9; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; background: #fff; box-shadow: 0 8px 30px rgba(0,0,0,.08); }
    .top { display: grid; grid-template-columns: 110px 1fr; gap: 24px; padding: 28px 32px; background: linear-gradient(135deg, #f0fdfa, #fff 60%); border-bottom: 3px solid var(--accent); }
    .avatar { width: 110px; height: 110px; border-radius: 16px; object-fit: cover; object-position: center 15%; }
    .top h1 { font-size: 22pt; font-weight: 700; color: var(--text); }
    .top .role { font-size: 10pt; color: var(--accent-dark); font-weight: 600; margin: 4px 0 12px; }
    .contact-row { display: flex; flex-wrap: wrap; gap: 6px 18px; font-size: 9pt; color: var(--muted); }
    .contact-row a { color: var(--accent-dark); text-decoration: none; }
    .contact-item { display: flex; align-items: center; gap: 5px; }
    .contact-item svg { width: 13px; height: 13px; color: var(--accent); }
    .body { display: grid; grid-template-columns: 32% 68%; }
    .sidebar { padding: 22px 18px 24px 24px; border-right: 1px solid var(--border); }
    .main { padding: 22px 24px 24px 18px; }
    .sidebar-section { margin-bottom: 16px; }
    .sidebar-section h2 { font-size: 8pt; font-weight: 700; text-transform: uppercase; letter-spacing: .1em; color: var(--accent); border-bottom: 1px solid var(--border); padding-bottom: 4px; margin-bottom: 8px; }
    .skill-tags { display: flex; flex-wrap: wrap; gap: 5px; }
    .skill-tag { font-size: 8.5pt; background: #f0fdfa; color: var(--accent-dark); border-radius: 20px; padding: 3px 8px; }
    .edu-degree { font-weight: 600; font-size: 9.5pt; }
    .edu-school, .edu-meta { font-size: 9pt; color: var(--muted); }
    .main h2 { font-size: 11pt; font-weight: 700; color: var(--accent-dark); border-bottom: 1px solid var(--border); padding-bottom: 4px; margin-bottom: 8px; }
    .job-title { color: var(--accent-dark); }
''' + SHARED_MAIN_CSS.replace('var(--text)', 'var(--text)').replace('var(--muted)', 'var(--muted)').replace('var(--border)', 'var(--border)')

    contact = "".join(
        f'<span class="contact-item">{ICONS[icon]}'
        + (f'<a href="{href}">{text}</a>' if href else text)
        + '</span>'
        for _, text, href, icon in CONTACT
    )

    body = f'''<div class="cv">
  <header class="top">
    <img class="avatar" src="avatar.png" alt="{NAME}">
    <div><h1>{NAME}</h1><div class="role">{ROLE}</div><div class="contact-row">{contact}</div></div>
  </header>
  <div class="body">
    <aside class="sidebar">
      {sidebar_skills(6)}
    </aside>
    <main class="main">
      {main_content(6)}
    </main>
  </div>
</div>'''
    return wrap(f"CV Modern — {NAME}", css, body)


def gen_dark():
    css = '''
    :root { --dark: #1a1f2e; --dark2: #252b3b; --gold: #c9a227; --text: #2d3748; --muted: #718096; --border: #e2e8f0; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: system-ui, sans-serif; font-size: 10.5pt; line-height: 1.45; color: var(--text); background: #cbd5e0; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; display: grid; grid-template-columns: 30% 70%; background: #fff; box-shadow: 0 6px 28px rgba(0,0,0,.18); }
    .sidebar { background: var(--dark); color: #e2e8f0; padding: 26px 18px; }
    .avatar { width: 100px; height: 100px; border-radius: 50%; object-fit: cover; object-position: center 15%; border: 3px solid var(--gold); display: block; margin: 0 auto 14px; }
    .sidebar h1 { font-size: 15pt; text-align: center; color: #fff; margin-bottom: 4px; }
    .sidebar .role { text-align: center; font-size: 8.5pt; color: var(--gold); font-weight: 600; margin-bottom: 20px; line-height: 1.35; padding-bottom: 16px; border-bottom: 1px solid var(--dark2); }
    .sidebar-section { margin-bottom: 18px; }
    .sidebar-section h2 { font-size: 7.5pt; text-transform: uppercase; letter-spacing: .14em; color: var(--gold); margin-bottom: 8px; font-weight: 700; }
    .contact-list { list-style: none; }
    .contact-list li { display: flex; gap: 8px; margin-bottom: 9px; font-size: 8.5pt; color: #a0aec0; }
    .contact-icon svg { width: 13px; height: 13px; color: var(--gold); flex-shrink: 0; margin-top: 2px; }
    .contact-list a { color: #cbd5e0; text-decoration: none; }
    .contact-label { display: block; font-size: 6.5pt; text-transform: uppercase; letter-spacing: .06em; color: var(--gold); }
    .skill-tags { display: flex; flex-wrap: wrap; gap: 4px; }
    .skill-tag { font-size: 7.5pt; padding: 3px 7px; background: var(--dark2); color: #e2e8f0; border-radius: 3px; border: 1px solid #3d4663; }
    .edu-degree { font-weight: 700; font-size: 9pt; color: #fff; }
    .edu-school, .edu-meta { font-size: 8.5pt; color: #a0aec0; }
    .main { padding: 26px 26px 22px 22px; }
    .main h2 { font-size: 11pt; color: var(--dark); border-bottom: 2px solid var(--gold); padding-bottom: 3px; margin-bottom: 8px; }
    .summary strong { color: var(--dark); }
    .job-title { color: var(--dark); }
    .job li::marker { color: var(--gold); }
    .project-header { color: var(--dark); }
    .ai-section .job li strong { color: var(--dark); }
''' + SHARED_MAIN_CSS

    body = f'''<div class="cv">
  <aside class="sidebar">
    <img class="avatar" src="avatar.png" alt="{NAME}">
    <h1>{NAME}</h1>
    <div class="role">{ROLE_BR}</div>
    <div class="sidebar-section"><h2>Liên hệ</h2><ul class="contact-list">
      {contact_sidebar(6)}
    </ul></div>
    {sidebar_skills(4)}
  </aside>
  <main class="main">
    {main_content(4)}
  </main>
</div>'''
    return wrap(f"CV Dark — {NAME}", css, body)


def gen_minimal():
    css = '''
    :root { --black: #111; --gray: #555; --light: #999; --rule: #ddd; --text: #111; --muted: #555; --border: #ddd; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: 'Segoe UI', system-ui, sans-serif; font-size: 10pt; line-height: 1.5; color: var(--black); background: #f5f5f5; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; background: #fff; padding: 36px 40px; box-shadow: 0 2px 12px rgba(0,0,0,.06); }
    .header { display: flex; gap: 28px; align-items: center; padding-bottom: 20px; border-bottom: 1px solid var(--black); margin-bottom: 20px; }
    .avatar { width: 88px; height: 88px; border-radius: 4px; object-fit: cover; object-position: center 15%; }
    .header h1 { font-size: 20pt; font-weight: 600; }
    .header .role { font-size: 9.5pt; color: var(--gray); margin: 3px 0 10px; }
    .contact { display: flex; flex-wrap: wrap; gap: 4px 16px; font-size: 8.5pt; color: var(--gray); }
    .contact a { color: var(--black); text-decoration: none; border-bottom: 1px solid var(--rule); }
    .ci { display: inline-flex; align-items: center; gap: 4px; }
    .ci svg { width: 11px; height: 11px; }
    .skills-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; margin-bottom: 20px; padding-bottom: 16px; border-bottom: 1px solid var(--rule); }
    .skills-grid h3 { font-size: 7pt; text-transform: uppercase; letter-spacing: .1em; color: var(--light); margin-bottom: 6px; }
    .skills-grid p { font-size: 8.5pt; color: var(--gray); line-height: 1.6; }
    h2 { font-size: 11pt; font-weight: 600; margin-bottom: 8px; margin-top: 18px; }
    .summary strong { color: var(--black); font-weight: 600; }
    .job-title { color: var(--black); }
''' + SHARED_MAIN_CSS

    contact = "".join(
        f'<span class="ci">{ICONS[icon]}' + (f'<a href="{href}">{text}</a>' if href else text) + '</span>'
        for _, text, href, icon in CONTACT
    )

    body = f'''<div class="cv">
  <header class="header">
    <img class="avatar" src="avatar.png" alt="{NAME}">
    <div>
      <h1>{NAME}</h1>
      <div class="role">{ROLE}</div>
      <div class="contact">{contact}</div>
    </div>
  </header>
  <div class="skills-grid">
    <div><h3>Lập trình &amp; ERP</h3><p>{" · ".join(SKILLS_ODOO)}</p></div>
    <div><h3>Công cụ &amp; AI</h3><p>{" · ".join(SKILLS_AI)}</p></div>
    <div><h3>Học vấn</h3><p>{EDU["degree"]}<br>{EDU["school"]}<br>{EDU["meta"]}</p></div>
  </div>
  {main_content(2)}
</div>'''
    return wrap(f"CV Minimal — {NAME}", css, body)


def gen_elegant():
    css = '''
    :root { --wine: #6b2737; --wine-l: #8b3a4a; --paper: #faf8f5; --text: #3d3d3d; --muted: #7a7a7a; --border: #d4cfc8; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: Georgia, serif; font-size: 10.5pt; line-height: 1.45; color: var(--text); background: #e8e4df; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; background: var(--paper); padding: 32px 36px; box-shadow: 0 4px 20px rgba(0,0,0,.1); }
    .head { text-align: center; padding-bottom: 18px; border-bottom: 1px solid var(--border); margin-bottom: 20px; }
    .avatar { width: 96px; height: 96px; border-radius: 50%; object-fit: cover; object-position: center 15%; border: 2px solid var(--wine); margin-bottom: 12px; }
    h1.name { font-size: 26pt; font-weight: 700; color: var(--wine); letter-spacing: .04em; }
    .role { font-size: 10pt; color: var(--wine-l); font-style: italic; margin: 4px 0 14px; }
    .contact { display: flex; flex-wrap: wrap; justify-content: center; gap: 6px 20px; font-size: 8.5pt; color: var(--muted); }
    .contact a { color: var(--wine-l); text-decoration: none; }
    .ci { display: inline-flex; align-items: center; gap: 4px; }
    .ci svg { width: 11px; height: 11px; color: var(--wine); }
    .cols { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 18px; }
    .cols h3 { font-size: 12pt; color: var(--wine); border-bottom: 1px solid var(--border); padding-bottom: 3px; margin-bottom: 8px; }
    .skill-line { font-size: 9pt; color: var(--muted); line-height: 1.65; font-family: system-ui, sans-serif; }
    h2 { font-size: 14pt; color: var(--wine); margin: 16px 0 8px; }
    .summary strong { color: var(--wine); }
    .job-title { color: var(--text); }
    .job-company { color: var(--wine-l); }
''' + SHARED_MAIN_CSS

    contact = "".join(
        f'<span class="ci">{ICONS[icon]}' + (f'<a href="{href}">{text}</a>' if href else text) + '</span>'
        for _, text, href, icon in CONTACT
    )

    body = f'''<div class="cv">
  <header class="head">
    <img class="avatar" src="avatar.png" alt="{NAME}">
    <h1 class="name">{NAME.upper()}</h1>
    <div class="role">{ROLE}</div>
    <div class="contact">{contact}</div>
  </header>
  <div class="cols">
    <div><h3>Lập trình &amp; ERP</h3><div class="skill-line">{" · ".join(SKILLS_ODOO)}</div></div>
    <div><h3>Công cụ &amp; Quy trình</h3><div class="skill-line">{" · ".join(SKILLS_AI)}<br><br>{" · ".join(SKILLS_SOFT)}</div></div>
  </div>
  <div class="cols" style="margin-bottom:0"><div><h3>Học vấn</h3><div class="skill-line"><strong>{EDU["degree"]}</strong><br>{EDU["school"]}<br>{EDU["meta"]}</div></div></div>
  {main_content(2)}
</div>'''
    return wrap(f"CV Elegant — {NAME}", css, body)


def gen_corporate():
    css = '''
    :root { --blue: #1565c0; --blue-d: #0d47a1; --text: #212121; --muted: #616161; --border: #e0e0e0; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: system-ui, sans-serif; font-size: 10.5pt; line-height: 1.45; color: var(--text); background: #eceff1; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; background: #fff; box-shadow: 0 4px 20px rgba(0,0,0,.1); }
    .banner { background: var(--blue); color: #fff; padding: 24px 32px; display: grid; grid-template-columns: 90px 1fr auto; gap: 20px; align-items: center; }
    .avatar { width: 90px; height: 90px; border-radius: 8px; object-fit: cover; object-position: center 15%; border: 2px solid rgba(255,255,255,.4); }
    .banner h1 { font-size: 20pt; font-weight: 700; }
    .banner .role { font-size: 9.5pt; opacity: .9; margin-top: 3px; }
    .banner-contact { font-size: 8.5pt; line-height: 1.7; text-align: right; }
    .banner-contact a { color: #fff; text-decoration: none; }
    .layout { display: grid; grid-template-columns: 32% 68%; }
    .sidebar { padding: 20px 18px 24px 24px; border-right: 1px solid var(--border); background: #fafafa; }
    .main { padding: 20px 24px 24px 18px; }
    .sidebar-section { margin-bottom: 16px; }
    .sidebar-section h2 { font-size: 8pt; font-weight: 700; text-transform: uppercase; letter-spacing: .1em; color: var(--blue); border-bottom: 1px solid var(--border); padding-bottom: 4px; margin-bottom: 8px; }
    .skill-tags { display: flex; flex-wrap: wrap; gap: 5px; }
    .skill-tag { font-size: 8.5pt; background: #fff; border: 1px solid var(--border); border-radius: 3px; padding: 3px 7px; }
    .edu-degree { font-weight: 600; font-size: 9.5pt; }
    .edu-school, .edu-meta { font-size: 9pt; color: var(--muted); }
    .main h2 { font-size: 11pt; color: var(--blue); border-left: 4px solid var(--blue); padding-left: 10px; margin-bottom: 10px; }
    .summary strong { color: var(--text); }
    .job-title { color: var(--blue-d); }
''' + SHARED_MAIN_CSS

    body = f'''<div class="cv">
  <header class="banner">
    <img class="avatar" src="avatar.png" alt="{NAME}">
    <div><h1>{NAME}</h1><div class="role">{ROLE}</div></div>
    <div class="banner-contact">
      duyquyencnt55@gmail.com<br>0963 108 848<br>An Biên, Hải Phòng, Việt Nam<br>
      <a href="https://github.com/duyquyen96">github.com/duyquyen96</a>
    </div>
  </header>
  <div class="layout">
    <aside class="sidebar">
      <div class="sidebar-section"><h2>Liên hệ</h2>
        <div class="edu-school">duyquyencnt55@gmail.com<br>0963 108 848<br>An Biên, Hải Phòng, Việt Nam<br>github.com/duyquyen96</div>
      </div>
      {sidebar_skills(6)}
    </aside>
    <main class="main">{main_content(6)}</main>
  </div>
</div>'''
    return wrap(f"CV Corporate — {NAME}", css, body)


def gen_creative():
    css = '''
    :root { --coral: #e85d4c; --coral-d: #c44335; --cream: #fffbf7; --char: #2c2c2c; --muted: #666; --text: #2c2c2c; --border: #f0e0dc; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: system-ui, sans-serif; font-size: 10.5pt; line-height: 1.45; color: var(--char); background: #f0ebe6; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; display: grid; grid-template-columns: 32% 68%; background: var(--cream); box-shadow: 0 6px 24px rgba(0,0,0,.1); }
    .sidebar { background: var(--coral); color: #fff; padding: 28px 20px; }
    .avatar { width: 110px; height: 110px; border-radius: 20px; object-fit: cover; object-position: center 15%; margin-bottom: 16px; }
    .sidebar h1 { font-size: 17pt; line-height: 1.2; margin-bottom: 6px; }
    .sidebar .role { font-size: 9pt; opacity: .92; margin-bottom: 22px; line-height: 1.4; padding-bottom: 18px; border-bottom: 1px solid rgba(255,255,255,.25); }
    .sidebar-section { margin-bottom: 18px; }
    .sidebar-section h2 { font-size: 7.5pt; text-transform: uppercase; letter-spacing: .12em; opacity: .75; margin-bottom: 8px; }
    .contact-list { list-style: none; }
    .contact-list li { display: flex; gap: 7px; margin-bottom: 9px; font-size: 8.5pt; }
    .contact-icon svg { width: 13px; height: 13px; flex-shrink: 0; margin-top: 2px; }
    .contact-list a { color: #fff; text-decoration: none; }
    .contact-label { display: block; font-size: 6.5pt; text-transform: uppercase; opacity: .75; }
    .skill-tags { display: flex; flex-wrap: wrap; gap: 4px; }
    .skill-tag { font-size: 7.5pt; padding: 3px 8px; background: rgba(255,255,255,.18); border-radius: 12px; }
    .edu-degree { font-weight: 700; font-size: 9pt; }
    .edu-school, .edu-meta { font-size: 8.5pt; opacity: .9; }
    .main { padding: 26px 22px 22px; }
    .main h2 { font-size: 13pt; color: var(--coral); margin-bottom: 8px; margin-top: 14px; }
    .main h2:first-child { margin-top: 0; }
    .summary strong { color: var(--coral-d); }
    .job-period { color: var(--coral); }
    .job li::marker { color: var(--coral); }
    .project-header { color: var(--coral-d); }
    .ai-section .job li strong { color: var(--coral-d); }
''' + SHARED_MAIN_CSS

    body = f'''<div class="cv">
  <aside class="sidebar">
    <img class="avatar" src="avatar.png" alt="{NAME}">
    <h1>{NAME}</h1>
    <div class="role">{ROLE_BR}</div>
    <div class="sidebar-section"><h2>Liên hệ</h2><ul class="contact-list">{contact_sidebar(6)}</ul></div>
    {sidebar_skills(4)}
  </aside>
  <main class="main">{main_content(4)}</main>
</div>'''
    return wrap(f"CV Creative — {NAME}", css, body)


def gen_tech():
    css = '''
    :root { --slate: #1e293b; --green: #22c55e; --green-d: #16a34a; --text: #1e293b; --muted: #64748b; --border: #e2e8f0; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: system-ui, sans-serif; font-size: 10.5pt; line-height: 1.45; color: var(--text); background: #0f172a; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; background: #fff; box-shadow: 0 8px 32px rgba(0,0,0,.3); }
    .top { background: var(--slate); color: #e2e8f0; padding: 20px 28px; display: flex; gap: 20px; align-items: center; position: relative; }
    .top::after { content: '// cv.json'; position: absolute; top: 8px; right: 28px; font-family: monospace; font-size: 7pt; color: var(--green); opacity: .6; }
    .avatar { width: 72px; height: 72px; border-radius: 6px; object-fit: cover; object-position: center 15%; border: 2px solid var(--green); }
    .top h1 { font-size: 16pt; font-weight: 700; }
    .top h1 span { color: var(--green); font-family: monospace; font-size: 10pt; font-weight: 400; }
    .top .role { font-size: 9pt; color: #94a3b8; margin-top: 2px; }
    .top .contact { margin-left: auto; text-align: right; font-family: monospace; font-size: 7.5pt; line-height: 1.8; color: #94a3b8; }
    .top .contact a { color: var(--green); text-decoration: none; }
    .layout { display: grid; grid-template-columns: 32% 68%; }
    .sidebar { padding: 18px 16px 22px 22px; border-right: 1px solid var(--border); background: #f8fafc; }
    .main { padding: 18px 22px 22px 16px; }
    .sidebar-section { margin-bottom: 14px; }
    .sidebar-section h2 { font-family: monospace; font-size: 7pt; text-transform: uppercase; letter-spacing: .08em; color: var(--green-d); margin-bottom: 6px; }
    .skill-tags { display: flex; flex-wrap: wrap; gap: 4px; }
    .skill-tag { font-size: 8pt; padding: 3px 7px; background: #fff; border: 1px solid var(--border); border-radius: 3px; font-family: monospace; }
    .edu-degree { font-weight: 600; font-size: 9pt; }
    .edu-school, .edu-meta { font-size: 8.5pt; color: var(--muted); }
    .main h2 { font-family: monospace; font-size: 9pt; margin-bottom: 8px; margin-top: 14px; }
    .main h2::before { content: '## '; color: var(--green-d); }
    .main h2:first-child { margin-top: 0; }
    .summary { padding: 10px 12px; background: #f8fafc; border-left: 3px solid var(--green); border-radius: 0 6px 6px 0; }
    .summary strong { color: var(--slate); }
    .job-period { font-family: monospace; font-size: 8pt; color: var(--green-d); }
''' + SHARED_MAIN_CSS

    body = f'''<div class="cv">
  <header class="top">
    <img class="avatar" src="avatar.png" alt="{NAME}">
    <div><h1>{NAME} <span>{{ python_dev }}</span></h1><div class="role">{ROLE}</div></div>
    <div class="contact">
      <a href="mailto:duyquyencnt55@gmail.com">duyquyencnt55@gmail.com</a><br>
      0963 108 848 · Hải Phòng<br>
      <a href="https://github.com/duyquyen96">github.com/duyquyen96</a>
    </div>
  </header>
  <div class="layout">
    <aside class="sidebar">{sidebar_skills(6)}</aside>
    <main class="main">{main_content(6)}</main>
  </div>
</div>'''
    return wrap(f"CV Tech — {NAME}", css, body)


def gen_nordic():
    css = '''
    :root { --ink: #2e3440; --muted: #4c566a; --frost: #eceff4; --accent: #5e81ac; --border: #d8dee9; --text: #2e3440; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: system-ui, sans-serif; font-size: 10.5pt; line-height: 1.5; color: var(--ink); background: var(--frost); print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; background: #fff; padding: 40px 44px; box-shadow: 0 2px 16px rgba(46,52,64,.08); }
    .head { display: flex; gap: 24px; align-items: center; margin-bottom: 28px; padding-bottom: 24px; border-bottom: 1px solid var(--border); }
    .avatar { width: 92px; height: 92px; border-radius: 50%; object-fit: cover; object-position: center 15%; }
    .head h1 { font-size: 21pt; font-weight: 300; letter-spacing: -.02em; color: var(--ink); }
    .head .role { font-size: 9.5pt; color: var(--accent); margin-top: 4px; font-weight: 500; }
    .contact { margin-top: 10px; display: flex; flex-wrap: wrap; gap: 4px 18px; font-size: 8.5pt; color: var(--muted); }
    .contact a { color: var(--accent); text-decoration: none; }
    .ci { display: inline-flex; align-items: center; gap: 5px; }
    .ci svg { width: 12px; height: 12px; color: var(--accent); }
    .layout { display: grid; grid-template-columns: 28% 72%; gap: 32px; }
    .sidebar-section { margin-bottom: 20px; }
    .sidebar-section h2 { font-size: 7pt; font-weight: 600; text-transform: uppercase; letter-spacing: .14em; color: var(--muted); margin-bottom: 8px; }
    .skill-tags { display: flex; flex-wrap: wrap; gap: 4px; }
    .skill-tag { font-size: 8pt; color: var(--ink); padding: 2px 0; border-bottom: 1px solid var(--border); width: 100%; }
    .edu-degree { font-weight: 600; font-size: 9pt; }
    .edu-school, .edu-meta { font-size: 8.5pt; color: var(--muted); }
    .main h2 { font-size: 8pt; font-weight: 600; text-transform: uppercase; letter-spacing: .12em; color: var(--muted); margin-bottom: 10px; margin-top: 20px; }
    .main h2:first-child { margin-top: 0; }
    .summary { font-size: 10pt; color: var(--muted); text-align: justify; }
    .summary strong { color: var(--ink); }
    .job { padding-left: 14px; border-left: 2px solid var(--border); }
    .job-title { color: var(--ink); font-weight: 600; }
    .job-period { color: var(--accent); }
    .project { padding-left: 14px; border-left: 2px solid var(--frost); }
''' + SHARED_MAIN_CSS

    contact = "".join(
        f'<span class="ci">{ICONS[icon]}' + (f'<a href="{href}">{text}</a>' if href else text) + '</span>'
        for _, text, href, icon in CONTACT
    )

    body = f'''<div class="cv">
  <header class="head">
    <img class="avatar" src="avatar.png" alt="{NAME}">
    <div><h1>{NAME}</h1><div class="role">{ROLE}</div><div class="contact">{contact}</div></div>
  </header>
  <div class="layout">
    <aside>{sidebar_skills(4)}</aside>
    <main class="main">{main_content(4)}</main>
  </div>
</div>'''
    return wrap(f"CV Nordic — {NAME}", css, body)


def gen_forest():
    css = '''
    :root { --forest: #1b4332; --forest-l: #2d6a4f; --sage: #d8f3dc; --text: #1b4332; --muted: #52796f; --border: #b7e4c7; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: Georgia, serif; font-size: 10.5pt; line-height: 1.45; color: var(--text); background: #e9f5e9; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; display: grid; grid-template-columns: 34% 66%; background: #fff; box-shadow: 0 4px 20px rgba(27,67,50,.12); }
    .sidebar { background: var(--forest); color: #fff; padding: 28px 20px; }
    .avatar { width: 105px; height: 105px; border-radius: 50%; object-fit: cover; object-position: center 15%; border: 3px solid var(--sage); display: block; margin: 0 auto 16px; }
    .sidebar h1 { font-size: 16pt; text-align: center; margin-bottom: 4px; }
    .sidebar .role { text-align: center; font-size: 8.5pt; color: var(--sage); margin-bottom: 22px; line-height: 1.35; padding-bottom: 16px; border-bottom: 1px solid var(--forest-l); }
    .sidebar-section { margin-bottom: 18px; }
    .sidebar-section h2 { font-size: 7.5pt; text-transform: uppercase; letter-spacing: .12em; color: var(--sage); margin-bottom: 8px; }
    .contact-list { list-style: none; }
    .contact-list li { display: flex; gap: 8px; margin-bottom: 9px; font-size: 8.5pt; color: #d8f3dc; }
    .contact-icon svg { width: 13px; height: 13px; color: var(--sage); flex-shrink: 0; margin-top: 2px; }
    .contact-list a { color: #fff; text-decoration: none; }
    .contact-label { display: block; font-size: 6.5pt; text-transform: uppercase; color: var(--sage); }
    .skill-tags { display: flex; flex-wrap: wrap; gap: 4px; }
    .skill-tag { font-size: 7.5pt; padding: 3px 8px; background: var(--forest-l); border-radius: 4px; }
    .edu-degree { font-weight: 700; font-size: 9pt; }
    .edu-school, .edu-meta { font-size: 8.5pt; color: #b7e4c7; }
    .main { padding: 26px 24px 22px; font-family: system-ui, sans-serif; }
    .main h2 { font-size: 11pt; color: var(--forest); border-bottom: 2px solid var(--sage); padding-bottom: 4px; margin-bottom: 10px; }
    .summary strong { color: var(--forest); }
    .job-title { color: var(--forest); }
    .job-period { color: var(--forest-l); }
    .job li::marker { color: var(--forest-l); }
    .project-header { color: var(--forest); }
    .ai-section .job li strong { color: var(--forest); }
''' + SHARED_MAIN_CSS.replace('var(--border)', 'var(--border)')

    body = f'''<div class="cv">
  <aside class="sidebar">
    <img class="avatar" src="avatar.png" alt="{NAME}">
    <h1>{NAME}</h1>
    <div class="role">{ROLE_BR}</div>
    <div class="sidebar-section"><h2>Liên hệ</h2><ul class="contact-list">{contact_sidebar(6)}</ul></div>
    {sidebar_skills(4)}
  </aside>
  <main class="main">{main_content(4)}</main>
</div>'''
    return wrap(f"CV Forest — {NAME}", css, body)


def gen_indigo():
    css = '''
    :root { --indigo: #4338ca; --indigo-l: #6366f1; --lavender: #eef2ff; --text: #1e1b4b; --muted: #64748b; --border: #c7d2fe; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: system-ui, sans-serif; font-size: 10.5pt; line-height: 1.45; color: var(--text); background: #e0e7ff; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; display: grid; grid-template-columns: 68% 32%; background: #fff; box-shadow: 0 6px 24px rgba(67,56,202,.15); }
    .main { padding: 28px 24px 24px 28px; }
    .sidebar { background: var(--lavender); padding: 28px 18px; border-left: 1px solid var(--border); }
    .sb-top { text-align: center; margin-bottom: 20px; padding-bottom: 16px; border-bottom: 1px solid var(--border); }
    .avatar { width: 100px; height: 100px; border-radius: 50%; object-fit: cover; object-position: center 15%; border: 3px solid var(--indigo-l); margin-bottom: 12px; }
    .sidebar h1 { font-size: 14pt; color: var(--indigo); margin-bottom: 4px; }
    .sidebar .role { font-size: 8.5pt; color: var(--indigo-l); font-weight: 600; line-height: 1.35; }
    .sidebar-section { margin-bottom: 16px; }
    .sidebar-section h2 { font-size: 7.5pt; text-transform: uppercase; letter-spacing: .1em; color: var(--indigo); margin-bottom: 8px; font-weight: 700; }
    .contact-list { list-style: none; }
    .contact-list li { margin-bottom: 8px; font-size: 8pt; color: var(--muted); }
    .contact-list a { color: var(--indigo); text-decoration: none; }
    .contact-label { display: block; font-size: 6.5pt; text-transform: uppercase; color: var(--indigo-l); font-weight: 600; }
    .skill-tags { display: flex; flex-wrap: wrap; gap: 4px; }
    .skill-tag { font-size: 7.5pt; padding: 3px 7px; background: #fff; border: 1px solid var(--border); border-radius: 4px; color: var(--text); }
    .edu-degree { font-weight: 600; font-size: 9pt; color: var(--text); }
    .edu-school, .edu-meta { font-size: 8.5pt; color: var(--muted); }
    .main h2 { font-size: 11pt; color: var(--indigo); margin-bottom: 8px; display: flex; align-items: center; gap: 8px; }
    .main h2::after { content: ''; flex: 1; height: 1px; background: var(--border); }
    .summary strong { color: var(--indigo); }
    .job-title { color: var(--indigo); }
    .job-period { color: var(--indigo-l); }
    .project-header { color: var(--indigo); }
    .ai-section .job li strong { color: var(--indigo); }
''' + SHARED_MAIN_CSS

    contact_simple = "".join(
        f'<li><span class="contact-label">{label}</span>'
        + (f'<a href="{href}">{text}</a>' if href else text)
        + '</li>'
        for label, text, href, _ in CONTACT
    )

    body = f'''<div class="cv">
  <main class="main">{main_content(4)}</main>
  <aside class="sidebar">
    <div class="sb-top">
      <img class="avatar" src="avatar.png" alt="{NAME}">
      <h1>{NAME}</h1>
      <div class="role">{ROLE_BR}</div>
    </div>
    <div class="sidebar-section"><h2>Liên hệ</h2><ul class="contact-list">{contact_simple}</ul></div>
    {sidebar_skills(4)}
  </aside>
</div>'''
    return wrap(f"CV Indigo — {NAME}", css, body)


def gen_newspaper():
    css = '''
    :root { --black: #1a1a1a; --gray: #555; --rule: #ccc; --text: #1a1a1a; --muted: #555; --border: #ccc; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: Georgia, 'Times New Roman', serif; font-size: 10.5pt; line-height: 1.45; color: var(--black); background: #f0f0f0; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; background: #fff; padding: 32px 36px; box-shadow: 0 2px 10px rgba(0,0,0,.1); }
    .masthead { text-align: center; border-top: 4px double var(--black); border-bottom: 4px double var(--black); padding: 16px 0; margin-bottom: 16px; }
    .masthead h1 { font-size: 24pt; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; }
    .masthead .role { font-size: 10pt; font-style: italic; color: var(--gray); margin: 4px 0 10px; }
    .masthead .contact { font-size: 8.5pt; color: var(--gray); display: flex; justify-content: center; flex-wrap: wrap; gap: 4px 16px; font-family: system-ui, sans-serif; }
    .masthead a { color: var(--black); }
    .masthead .avatar { width: 80px; height: 80px; border-radius: 4px; object-fit: cover; object-position: center 15%; float: left; margin: 0 16px 8px 0; border: 1px solid var(--rule); }
    .skills-row { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; padding: 12px 0; border-bottom: 1px solid var(--rule); margin-bottom: 14px; font-family: system-ui, sans-serif; }
    .skills-row h3 { font-size: 7pt; text-transform: uppercase; letter-spacing: .1em; border-bottom: 1px solid var(--black); padding-bottom: 2px; margin-bottom: 5px; }
    .skills-row p { font-size: 8.5pt; color: var(--gray); line-height: 1.55; }
    h2 { font-size: 11pt; font-variant: small-caps; letter-spacing: .08em; border-bottom: 1px solid var(--black); padding-bottom: 3px; margin: 14px 0 8px; }
    .summary { font-size: 10pt; text-align: justify; column-count: 1; }
    .summary strong { font-weight: 700; }
    .two-col { column-count: 2; column-gap: 24px; }
    .job { break-inside: avoid; margin-bottom: 10px; }
    .job-title { font-weight: 700; font-size: 10pt; }
    .job-period { font-size: 8.5pt; color: var(--gray); font-style: italic; }
    .job-company { font-size: 9pt; font-style: italic; }
    .job ul { padding-left: 14px; font-family: system-ui, sans-serif; font-size: 9pt; }
    .project { break-inside: avoid; margin-bottom: 8px; font-size: 9.5pt; }
    .project-header { font-weight: 700; }
    .project-meta { font-weight: 400; color: var(--gray); font-size: 9pt; }
    .project ul { font-family: system-ui, sans-serif; font-size: 9pt; padding-left: 14px; }
''' + SHARED_MAIN_CSS

    contact = " · ".join(
        f'<a href="{href}">{text}</a>' if href else text for _, text, href, _ in CONTACT
    )

    body = f'''<div class="cv">
  <header class="masthead">
    <img class="avatar" src="avatar.png" alt="{NAME}">
    <h1>{NAME}</h1>
    <div class="role">{ROLE}</div>
    <div class="contact">{contact}</div>
  </header>
  <div class="skills-row">
    <div><h3>Lập trình / ERP</h3><p>{" · ".join(SKILLS_ODOO)}</p></div>
    <div><h3>Công cụ &amp; AI</h3><p>{" · ".join(SKILLS_AI)}</p></div>
    <div><h3>Học vấn</h3><p>{EDU["degree"]}<br>{EDU["school"]}<br>{EDU["meta"]}</p></div>
  </div>
  <h2>Tóm tắt</h2>
  <p class="summary">{SUMMARY}</p>
{PERSONAL}
  <h2>Kinh nghiệm làm việc</h2>
  <div class="two-col">{jobs_html(2)}</div>
  <h2>Kỹ năng bổ sung</h2>
  <div class="job"><ul>{"".join(f"<li>{b}</li>" for b in AI_BULLETS)}</ul></div>
  <h2>Dự án tiêu biểu</h2>
  <p class="section-note">{PROJECT_NOTE}</p>
  <div class="two-col">{projects_html(2)}
  <div class="projects-more" style="column-span:all">
    <span class="projects-more-label">Các dự án &amp; hạng mục khác đã tham gia:</span>
    <div class="projects-tags">{"".join(f"<span>{t}</span>" for t in MORE_TAGS)}</div>
    {MORE_TEXT}
    <span class="projects-cta">{MORE_CTA}</span>
  </div></div>
</div>'''
    return wrap(f"CV Newspaper — {NAME}", css, body)


def gen_geometric():
    css = '''
    :root { --orange: #ea580c; --orange-l: #fb923c; --dark: #1c1917; --text: #292524; --muted: #78716c; --border: #e7e5e4; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: system-ui, sans-serif; font-size: 10.5pt; line-height: 1.45; color: var(--text); background: #fafaf9; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; background: #fff; box-shadow: 0 4px 24px rgba(0,0,0,.08); overflow: hidden; }
    .accent-bar { height: 8px; background: linear-gradient(90deg, var(--orange), var(--orange-l), var(--dark)); }
    .top { padding: 24px 28px; display: grid; grid-template-columns: 1fr auto; gap: 20px; align-items: start; }
    .top-left { display: flex; gap: 20px; align-items: center; }
    .avatar { width: 88px; height: 88px; clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%); object-fit: cover; object-position: center 15%; }
    .top h1 { font-size: 20pt; font-weight: 800; color: var(--dark); letter-spacing: -.03em; }
    .top .role { font-size: 9.5pt; color: var(--orange); font-weight: 600; margin-top: 3px; }
    .contact-block { font-size: 8pt; color: var(--muted); line-height: 1.7; text-align: right; }
    .contact-block a { color: var(--orange); text-decoration: none; font-weight: 500; }
    .body { display: grid; grid-template-columns: 30% 70%; }
    .sidebar { background: var(--dark); color: #fafaf9; padding: 22px 18px; }
    .sidebar-section { margin-bottom: 16px; }
    .sidebar-section h2 { font-size: 7pt; text-transform: uppercase; letter-spacing: .14em; color: var(--orange-l); margin-bottom: 8px; font-weight: 700; }
    .skill-tags { display: flex; flex-wrap: wrap; gap: 4px; }
    .skill-tag { font-size: 7.5pt; padding: 3px 7px; background: #292524; border-left: 2px solid var(--orange); color: #e7e5e4; }
    .edu-degree { font-weight: 700; font-size: 9pt; color: #fff; }
    .edu-school, .edu-meta { font-size: 8.5pt; color: #a8a29e; }
    .main { padding: 22px 24px 24px 20px; }
    .main h2 { font-size: 10pt; font-weight: 800; text-transform: uppercase; letter-spacing: .06em; color: var(--dark); margin-bottom: 8px; margin-top: 14px; display: inline-block; border-bottom: 3px solid var(--orange); padding-bottom: 2px; }
    .main h2:first-child { margin-top: 0; }
    .summary strong { color: var(--orange); }
    .job-title { color: var(--dark); font-weight: 700; }
    .job-period { color: var(--orange); font-weight: 600; }
    .job li::marker { color: var(--orange); }
    .project-header { color: var(--dark); }
    .ai-section .job li strong { color: var(--orange); }
''' + SHARED_MAIN_CSS

    body = f'''<div class="cv">
  <div class="accent-bar"></div>
  <header class="top">
    <div class="top-left">
      <img class="avatar" src="avatar.png" alt="{NAME}">
      <div><h1>{NAME}</h1><div class="role">{ROLE}</div></div>
    </div>
    <div class="contact-block">
      <a href="mailto:duyquyencnt55@gmail.com">duyquyencnt55@gmail.com</a><br>
      0963 108 848<br>An Biên, Hải Phòng, Việt Nam<br>
      <a href="https://github.com/duyquyen96">github.com/duyquyen96</a>
    </div>
  </header>
  <div class="body">
    <aside class="sidebar">{sidebar_skills(4)}</aside>
    <main class="main">{main_content(4)}</main>
  </div>
</div>'''
    return wrap(f"CV Geometric — {NAME}", css, body)


def gen_ocean():
    css = '''
    :root { --ocean: #0369a1; --ocean-l: #0ea5e9; --sky: #f0f9ff; --text: #0c4a6e; --muted: #64748b; --border: #bae6fd; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: system-ui, sans-serif; font-size: 10.5pt; line-height: 1.45; color: var(--text); background: #e0f2fe; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; background: #fff; border-radius: 8px; overflow: hidden; box-shadow: 0 8px 30px rgba(3,105,161,.15); }
    .wave { height: 6px; background: repeating-linear-gradient(90deg, var(--ocean), var(--ocean-l) 20px, var(--ocean) 40px); }
    .wrap { padding: 26px 28px 24px; }
    .profile { display: flex; gap: 22px; background: var(--sky); border-radius: 12px; padding: 20px; margin-bottom: 20px; }
    .avatar { width: 96px; height: 96px; border-radius: 50%; object-fit: cover; object-position: center 15%; border: 4px solid #fff; box-shadow: 0 2px 12px rgba(3,105,161,.2); flex-shrink: 0; }
    .profile h1 { font-size: 19pt; font-weight: 700; color: var(--ocean); }
    .profile .role { font-size: 9.5pt; color: var(--ocean-l); font-weight: 600; margin: 3px 0 10px; }
    .profile .contact { font-size: 8.5pt; color: var(--muted); display: flex; flex-wrap: wrap; gap: 4px 14px; }
    .profile a { color: var(--ocean); text-decoration: none; }
    .ci { display: inline-flex; align-items: center; gap: 4px; }
    .ci svg { width: 11px; height: 11px; color: var(--ocean-l); }
    .chips { display: flex; flex-wrap: wrap; gap: 16px; margin-bottom: 18px; padding-bottom: 16px; border-bottom: 1px dashed var(--border); }
    .chip-group h3 { font-size: 7pt; text-transform: uppercase; letter-spacing: .1em; color: var(--ocean-l); margin-bottom: 5px; }
    .chip-group p { font-size: 8.5pt; color: var(--muted); line-height: 1.6; max-width: 200px; }
    .main h2 { font-size: 10pt; color: var(--ocean); background: var(--sky); display: inline-block; padding: 4px 12px; border-radius: 4px; margin-bottom: 10px; margin-top: 14px; }
    .main h2:first-child { margin-top: 0; }
    .summary { background: var(--sky); padding: 12px 14px; border-radius: 8px; font-size: 10pt; text-align: justify; }
    .summary strong { color: var(--ocean); }
    .job { background: #fff; border: 1px solid var(--border); border-radius: 6px; padding: 10px 12px; }
    .job-title { color: var(--ocean); }
    .job-period { color: var(--ocean-l); }
    .project { border: 1px solid var(--border); border-radius: 6px; padding: 8px 10px; background: #fafcff; }
    .project-header { color: var(--ocean); }
    .ai-section .job li strong { color: var(--ocean); }
''' + SHARED_MAIN_CSS.replace('.job { margin-bottom: 14px; }', '.job { margin-bottom: 10px; }')

    contact = "".join(
        f'<span class="ci">{ICONS[icon]}' + (f'<a href="{href}">{text}</a>' if href else text) + '</span>'
        for _, text, href, icon in CONTACT
    )

    body = f'''<div class="cv">
  <div class="wave"></div>
  <div class="wrap">
    <div class="profile">
      <img class="avatar" src="avatar.png" alt="{NAME}">
      <div>
        <h1>{NAME}</h1>
        <div class="role">{ROLE}</div>
        <div class="contact">{contact}</div>
      </div>
    </div>
    <div class="chips">
      <div class="chip-group"><h3>Lập trình / ERP</h3><p>{" · ".join(SKILLS_ODOO)}</p></div>
      <div class="chip-group"><h3>Công cụ &amp; AI</h3><p>{" · ".join(SKILLS_AI)}</p></div>
      <div class="chip-group"><h3>Quy trình &amp; Tài liệu</h3><p>{" · ".join(SKILLS_SOFT)}</p></div>
      <div class="chip-group"><h3>Học vấn</h3><p>{EDU["degree"]}<br>{EDU["school"]}<br>{EDU["meta"]}</p></div>
    </div>
    <main class="main">{main_content(4)}</main>
  </div>
</div>'''
    css += """
    @media print {
      .wrap { padding: 16px 28px 0; }
      .job li, .project li { font-size: 9pt; line-height: 1.35; }
      .projects-more { margin-top: 8px; }
      .profile { margin-bottom: 14px; }
      .chips { gap: 12px; margin-bottom: 12px; padding-bottom: 10px; }
      .chip-group p { line-height: 1.4; }
      .main-section { margin-bottom: 12px; }
      .main h2 { margin-top: 8px; margin-bottom: 7px; }
      .summary { padding: 8px 10px; }
      .job { padding: 7px 10px; margin-bottom: 10px; }
      .project { padding: 5px 8px; margin-bottom: 7px; }
    }
    """.rstrip()
    return wrap(f"CV Ocean — {NAME}", css, body)


CLASSIC_CSS = "\n    :root {\n      --navy: #1e3a5f;\n      --navy-light: #2c5282;\n      --text: #2d3748;\n      --text-muted: #4a5568;\n      --sidebar-bg: #f8f9fa;\n      --border: #cbd5e0;\n      --accent: #1e3a5f;\n    }\n\n    * {\n      margin: 0;\n      padding: 0;\n      box-sizing: border-box;\n    }\n\n    body {\n      font-family: 'Source Sans 3', system-ui, -apple-system, sans-serif;\n      font-size: 10.5pt;\n      line-height: 1.45;\n      color: var(--text);\n      background: #e2e8f0;\n      -webkit-print-color-adjust: exact;\n      print-color-adjust: exact;\n    }\n\n    .cv-page {\n      max-width: 210mm;\n      min-height: 297mm;\n      margin: 16px auto;\n      background: #fff;\n      display: grid;\n      grid-template-columns: 32% 68%;\n      box-shadow: 0 4px 24px rgba(0, 0, 0, 0.12);\n    }\n\n    /* ── Sidebar ── */\n    .sidebar {\n      background: var(--sidebar-bg);\n      border-right: 2px solid var(--navy);\n      padding: 28px 20px;\n    }\n\n    .sidebar-header {\n      margin-bottom: 24px;\n      padding-bottom: 16px;\n      border-bottom: 1px solid var(--border);\n      text-align: center;\n    }\n\n    .avatar {\n      width: 120px;\n      height: 120px;\n      border-radius: 50%;\n      object-fit: cover;\n      object-position: center 15%;\n      border: 3px solid var(--navy);\n      margin: 0 auto 14px;\n      display: block;\n      box-shadow: 0 2px 8px rgba(30, 58, 95, 0.15);\n    }\n\n    .sidebar-header h1 {\n      font-family: 'Merriweather', Georgia, serif;\n      font-size: 17pt;\n      font-weight: 700;\n      color: var(--navy);\n      line-height: 1.25;\n      margin-bottom: 6px;\n    }\n\n    .sidebar-header .title {\n      font-size: 9.5pt;\n      font-weight: 600;\n      color: var(--navy-light);\n      line-height: 1.35;\n    }\n\n    .sidebar-section {\n      margin-bottom: 20px;\n    }\n\n    .sidebar-section h2 {\n      font-family: 'Merriweather', Georgia, serif;\n      font-size: 8.5pt;\n      font-weight: 700;\n      text-transform: uppercase;\n      letter-spacing: 0.1em;\n      color: var(--navy);\n      border-bottom: 1px solid var(--border);\n      padding-bottom: 4px;\n      margin-bottom: 10px;\n    }\n\n    .contact-list {\n      list-style: none;\n    }\n\n    .contact-list li {\n      display: flex;\n      align-items: flex-start;\n      gap: 9px;\n      margin-bottom: 10px;\n      font-size: 9.5pt;\n      color: var(--text-muted);\n      word-break: break-word;\n    }\n\n    .contact-list li:last-child {\n      margin-bottom: 0;\n    }\n\n    .contact-icon {\n      flex-shrink: 0;\n      width: 15px;\n      height: 15px;\n      margin-top: 2px;\n      color: var(--navy);\n    }\n\n    .contact-icon svg {\n      display: block;\n      width: 100%;\n      height: 100%;\n    }\n\n    .contact-body {\n      flex: 1;\n      min-width: 0;\n    }\n\n    .contact-list a {\n      color: var(--navy-light);\n      text-decoration: none;\n    }\n\n    .contact-list a:hover {\n      text-decoration: underline;\n    }\n\n    .contact-label {\n      display: block;\n      font-size: 7pt;\n      text-transform: uppercase;\n      letter-spacing: 0.06em;\n      color: var(--navy);\n      font-weight: 600;\n      margin-bottom: 1px;\n    }\n\n    .skill-tags {\n      display: flex;\n      flex-wrap: wrap;\n      gap: 5px;\n    }\n\n    .skill-tag {\n      font-size: 8.5pt;\n      background: #fff;\n      border: 1px solid var(--border);\n      border-radius: 3px;\n      padding: 3px 7px;\n      color: var(--text);\n      line-height: 1.3;\n    }\n\n    .edu-degree {\n      font-weight: 600;\n      font-size: 9.5pt;\n      color: var(--text);\n      margin-bottom: 2px;\n    }\n\n    .edu-school {\n      font-size: 9.5pt;\n      color: var(--text-muted);\n    }\n\n    .edu-meta {\n      font-size: 8.5pt;\n      color: var(--text-muted);\n      margin-top: 3px;\n    }\n\n    /* ── Main ── */\n    .main {\n      padding: 28px 28px 24px 24px;\n    }\n\n    .main-section {\n      margin-bottom: 18px;\n    }\n\n    .main-section:last-child {\n      margin-bottom: 0;\n    }\n\n    .main-section h2 {\n      font-family: 'Merriweather', Georgia, serif;\n      font-size: 10pt;\n      font-weight: 700;\n      text-transform: uppercase;\n      letter-spacing: 0.08em;\n      color: var(--navy);\n      border-bottom: 2px solid var(--navy);\n      padding-bottom: 4px;\n      margin-bottom: 6px;\n    }\n\n    .section-note {\n      font-size: 8.5pt;\n      color: var(--text-muted);\n      font-style: italic;\n      margin-bottom: 12px;\n      line-height: 1.4;\n    }\n\n    .summary {\n      font-size: 10pt;\n      color: var(--text);\n      text-align: justify;\n      line-height: 1.5;\n    }\n\n    .summary strong {\n      color: var(--navy);\n      font-weight: 700;\n    }\n\n    /* Experience */\n    .job {\n      margin-bottom: 14px;\n    }\n\n    .job:last-child {\n      margin-bottom: 0;\n    }\n\n    .job-header {\n      display: flex;\n      justify-content: space-between;\n      align-items: baseline;\n      flex-wrap: wrap;\n      gap: 4px 12px;\n      margin-bottom: 2px;\n    }\n\n    .job-title {\n      font-weight: 700;\n      font-size: 10.5pt;\n      color: var(--navy);\n    }\n\n    .job-period {\n      font-size: 9pt;\n      color: var(--text-muted);\n      white-space: nowrap;\n      font-weight: 600;\n    }\n\n    .job-company {\n      font-size: 9.5pt;\n      color: var(--text-muted);\n      font-style: italic;\n      margin-bottom: 6px;\n    }\n\n    .job ul {\n      padding-left: 16px;\n    }\n\n    .job li {\n      font-size: 9.5pt;\n      color: var(--text);\n      margin-bottom: 3px;\n      line-height: 1.4;\n    }\n\n    .job li::marker {\n      color: var(--navy-light);\n    }\n\n    /* Projects */\n    .project {\n      margin-bottom: 11px;\n      padding-left: 10px;\n      border-left: 3px solid var(--border);\n    }\n\n    .project:last-child {\n      margin-bottom: 0;\n    }\n\n    .project-header {\n      font-size: 9.5pt;\n      font-weight: 700;\n      color: var(--navy);\n      margin-bottom: 4px;\n      line-height: 1.35;\n    }\n\n    .project-meta {\n      font-weight: 400;\n      color: var(--text-muted);\n      font-size: 9pt;\n    }\n\n    .project ul {\n      padding-left: 14px;\n    }\n\n    .project li {\n      font-size: 9.5pt;\n      margin-bottom: 2px;\n      line-height: 1.4;\n    }\n\n    .projects-more {\n      margin-top: 12px;\n      padding: 0;\n      font-size: 9pt;\n      line-height: 1.45;\n      color: var(--text-muted);\n    }\n\n    .projects-more-label {\n      color: var(--text);\n      font-weight: 400;\n    }\n\n    .projects-tags {\n      display: flex;\n      flex-wrap: wrap;\n      gap: 4px;\n      margin: 6px 0 8px;\n    }\n\n    .projects-tags span {\n      font-size: 8pt;\n      background: #fff;\n      border: 1px solid var(--border);\n      border-radius: 3px;\n      padding: 2px 6px;\n      color: var(--text);\n    }\n\n    .projects-cta {\n      display: block;\n      font-size: 8.5pt;\n      color: var(--text-muted);\n      font-weight: 400;\n      font-style: italic;\n    }\n\n    /* AI section highlight */\n    .ai-section .job li strong {\n      color: var(--navy);\n    }\n\n    /* Mobile + iframe embed (screen only — never affect PDF/print) */\n    html { -webkit-text-size-adjust: 100%; }\n\n    @media screen {\n      body {\n        container-type: inline-size;\n        container-name: cv-root;\n        min-width: 0;\n        overflow-x: hidden;\n      }\n      .cv-page { width: 100%; min-width: 0; }\n    }\n\n    @media screen {\n    @container cv-root (max-width: 600px) {\n      body { background: #fff; font-size: 10pt; overflow-x: hidden; }\n      .cv-page {\n        margin: 0;\n        width: 100%;\n        max-width: 100%;\n        min-width: 0;\n        min-height: auto;\n        box-shadow: none;\n        display: block !important;\n        grid-template-columns: none !important;\n      }\n      .sidebar {\n        width: 100%;\n        border-right: none;\n        border-bottom: 2px solid var(--navy);\n        padding: 20px 16px;\n      }\n      .main { padding: 20px 16px; width: 100%; }\n      .job-header { flex-direction: column; align-items: flex-start; gap: 2px; }\n      .job-period { white-space: normal; }\n      .contact-list a, .contact-body { overflow-wrap: anywhere; }\n    }\n    }\n\n    @media screen and (max-width: 600px) {\n      body { background: #fff; font-size: 10pt; overflow-x: hidden; }\n      .cv-page {\n        margin: 0;\n        width: 100%;\n        max-width: 100%;\n        min-width: 0;\n        min-height: auto;\n        box-shadow: none;\n        display: block !important;\n        grid-template-columns: none !important;\n      }\n      .sidebar {\n        width: 100%;\n        border-right: none;\n        border-bottom: 2px solid var(--navy);\n        padding: 20px 16px;\n      }\n      .main { padding: 20px 16px; width: 100%; }\n      .job-header { flex-direction: column; align-items: flex-start; gap: 2px; }\n      .job-period { white-space: normal; }\n      .contact-list a, .contact-body { overflow-wrap: anywhere; }\n    }\n\n    html.cv-embed body { background: #fff; font-size: 10pt; overflow-x: hidden; }\n    html.cv-embed .cv-page {\n      margin: 0;\n      width: 100%;\n      max-width: 100%;\n      min-width: 0;\n      min-height: auto;\n      box-shadow: none;\n      display: block !important;\n      grid-template-columns: none !important;\n    }\n    html.cv-embed .sidebar {\n      width: 100%;\n      border-right: none;\n      border-bottom: 2px solid var(--navy);\n      padding: 20px 16px;\n    }\n    html.cv-embed .main { padding: 20px 16px; width: 100%; }\n    html.cv-embed .job-header { flex-direction: column; align-items: flex-start; gap: 2px; }\n    html.cv-embed .job-period { white-space: normal; }\n    html.cv-embed .contact-list a, html.cv-embed .contact-body { overflow-wrap: anywhere; }\n\n    /* Print */\n    @media print {\n      body {\n        background: #fff;\n        font-size: 10pt;\n        -webkit-print-color-adjust: exact;\n        print-color-adjust: exact;\n      }\n\n      html, body {\n        margin: 0;\n        padding: 0;\n      }\n\n      body {\n        container-type: normal;\n      }\n\n      .cv-page {\n        margin: 0;\n        box-shadow: none;\n        max-width: none;\n        width: 100%;\n        min-height: auto;\n        overflow: visible;\n        display: grid;\n        grid-template-columns: 32% 68%;\n      }\n\n      .sidebar {\n        border-right: 2px solid var(--navy);\n        border-bottom: none;\n        width: auto;\n      }\n\n      .job-header {\n        flex-direction: row;\n        align-items: baseline;\n      }\n\n      .job-period {\n        white-space: nowrap;\n      }\n\n      @page {\n        size: A4;\n        margin: 0;\n      }\n\n      .summary,\n      .projects-more {\n        break-inside: avoid;\n        page-break-inside: avoid;\n      }\n\n      .main-section > h2 {\n        break-after: avoid;\n        page-break-after: avoid;\n      }\n\n      .job {\n        break-inside: avoid;\n        page-break-inside: avoid;\n      }\n\n      .project {\n        break-inside: avoid;\n        page-break-inside: avoid;\n      }\n    }\n  "

def gen_classic():
    css = CLASSIC_CSS
    body = f'''<div class="cv-page"><aside class="sidebar">
      <div class="sidebar-header"><img class="avatar" src="avatar.png" alt="{NAME}">
      <h1>{NAME}</h1><div class="title">{ROLE_BR}</div></div>
      <div class="sidebar-section"><h2>Liên hệ</h2><ul class="contact-list">{contact_sidebar()}</ul></div>
      {sidebar_skills()}</aside><main class="main">{main_content()}</main></div>'''
    return wrap(f"CV - {NAME}", css, body)


STYLES = {
    "nguyen-duy-quyen-cv.html": gen_classic,
    "nguyen-duy-quyen-cv-modern.html": gen_modern,
    "nguyen-duy-quyen-cv-dark.html": gen_dark,
    "nguyen-duy-quyen-cv-minimal.html": gen_minimal,
    "nguyen-duy-quyen-cv-elegant.html": gen_elegant,
    "nguyen-duy-quyen-cv-corporate.html": gen_corporate,
    "nguyen-duy-quyen-cv-creative.html": gen_creative,
    "nguyen-duy-quyen-cv-tech.html": gen_tech,
    "nguyen-duy-quyen-cv-nordic.html": gen_nordic,
    "nguyen-duy-quyen-cv-forest.html": gen_forest,
    "nguyen-duy-quyen-cv-indigo.html": gen_indigo,
    "nguyen-duy-quyen-cv-newspaper.html": gen_newspaper,
    "nguyen-duy-quyen-cv-geometric.html": gen_geometric,
    "nguyen-duy-quyen-cv-ocean.html": gen_ocean,
}


ALL_CV_HTML = list(STYLES)

PDF_EXPORT_CSS = """
    /* PDF export overrides */
    @page { size: A4; margin: 8mm 0; }
    html, body {
      margin: 0 !important;
      padding: 0 !important;
      background: #fff !important;
      container-type: normal !important;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }
    .cv-page, .cv {
      margin: 0 !important;
      box-shadow: none !important;
      max-width: none !important;
      width: 100% !important;
      min-height: auto !important;
      border-radius: 0 !important;
      overflow: visible !important;
    }
    .cv-page {
      display: grid !important;
      grid-template-columns: 32% 68% !important;
    }
    .sidebar, aside.sidebar {
      width: auto !important;
      border-bottom: none !important;
    }
    .body, .layout {
      display: grid !important;
    }
    .job-header {
      flex-direction: row !important;
      align-items: baseline !important;
    }
    .job-period {
      white-space: nowrap !important;
    }
    .job, .project, .profile, .chips, .projects-more, .summary {
      break-inside: avoid !important;
      page-break-inside: avoid !important;
    }
    .main-section > h2, .main h2, .cv > h2, .section-note {
      break-after: avoid !important;
      page-break-after: avoid !important;
    }
"""


def _avatar_data_uri():
    import base64

    avatar_path = DIR / "avatar.png"
    if not avatar_path.exists():
        return None
    data = avatar_path.read_bytes()
    if data[:3] == b"\xff\xd8\xff":
        mime = "image/jpeg"
    elif data[:8] == b"\x89PNG\r\n\x1a\n":
        mime = "image/png"
    else:
        mime = "image/png"
    encoded = base64.b64encode(data).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def _prepare_pdf_html(html_path):
    import re

    content = html_path.read_text(encoding="utf-8")
    if "/* PDF export overrides */" not in content:
        content = content.replace("</style>", PDF_EXPORT_CSS + "\n  </style>", 1)
    avatar_src = _avatar_data_uri()
    if avatar_src:
        content = content.replace('src="avatar.png"', f'src="{avatar_src}"')
        content = re.sub(
            r'src="(?:file://[^"]*avatar\.png|data:image/[^;]+;base64,[^"]+)"',
            f'src="{avatar_src}"',
            content,
        )
    tmp_dir = DIR / "work" / "pdf-html"
    tmp_dir.mkdir(parents=True, exist_ok=True)
    tmp_path = tmp_dir / html_path.name
    tmp_path.write_text(content, encoding="utf-8")
    return tmp_path


def _find_chrome():
    import shutil

    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser"):
        path = shutil.which(name)
        if path:
            return path
    return None


def export_pdfs():
    import shutil
    import subprocess

    pdf_dir = DIR / "pdf"
    pdf_dir.mkdir(exist_ok=True)
    chrome = _find_chrome()
    wkhtml_bin = shutil.which("wkhtmltopdf")
    if not chrome and not wkhtml_bin:
        print("✗ Không tìm thấy Chrome hay wkhtmltopdf — bỏ qua xuất PDF")
        return

    engine = "Chrome headless" if chrome else "wkhtmltopdf"
    print(f"PDF engine: {engine}")

    for html_name in ALL_CV_HTML:
        html_path = DIR / html_name
        if not html_path.exists():
            print(f"✗ Bỏ qua (không có file): {html_name}")
            continue
        pdf_name = html_name.replace(".html", ".pdf")
        pdf_path = pdf_dir / pdf_name
        pdf_html_path = _prepare_pdf_html(html_path)
        if chrome:
            cmd = [
                chrome,
                "--headless=new",
                f"--user-data-dir={DIR / 'work' / 'chrome-profile'}",
                "--disable-gpu",
                "--allow-file-access-from-files",
                "--run-all-compositor-stages-before-draw",
                "--virtual-time-budget=10000",
                "--no-pdf-header-footer",
                f"--print-to-pdf={pdf_path}",
                pdf_html_path.resolve().as_uri(),
            ]
        else:
            cmd = [
                wkhtml_bin,
                "--quiet",
                "--page-size", "A4",
                "--margin-top", "0",
                "--margin-bottom", "0",
                "--margin-left", "0",
                "--margin-right", "0",
                "--encoding", "UTF-8",
                "--disable-smart-shrinking",
                "--enable-local-file-access",
                str(pdf_html_path),
                str(pdf_path),
            ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
        if result.returncode == 0 and pdf_path.exists():
            print(f"✓ pdf/{pdf_name}")
        else:
            err = result.stderr.strip() or result.stdout.strip() or "lỗi không xác định"
            print(f"✗ pdf/{pdf_name}: {err}")


def main(export_pdf=True):
    for filename, generator in STYLES.items():
        path = DIR / filename
        path.write_text("\n".join(line.rstrip() for line in generator().splitlines()) + "\n", encoding="utf-8")
        print(f"✓ {filename}")
    if export_pdf:
        print("— Xuất PDF —")
        export_pdfs()


if __name__ == "__main__":
    import sys
    pdf_only = "--pdf-only" in sys.argv
    if pdf_only:
        export_pdfs()
    else:
        main(export_pdf=True)
