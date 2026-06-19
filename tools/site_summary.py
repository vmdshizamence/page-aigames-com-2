import json
from typing import List, Dict

def load_site_profile() -> Dict:
    return {
        "title": "爱游戏体育",
        "url": "https://page-aigames.com",
        "keywords": ["爱游戏体育", "体育竞技", "在线娱乐", "游戏平台"],
        "tags": ["体育", "游戏", "娱乐", "在线"],
        "description": "爱游戏体育是一个专注于体育赛事与电子竞技的综合游戏平台，为用户提供丰富的在线娱乐体验。",
        "language": "zh-CN",
        "category": "游戏"
    }

def extract_summary(data: Dict) -> str:
    title = data.get("title", "未知站点")
    url = data.get("url", "无链接")
    keywords = ", ".join(data.get("keywords", []))
    tags = ", ".join(data.get("tags", []))
    desc = data.get("description", "暂无说明")
    lang = data.get("language", "未知")
    category = data.get("category", "未分类")

    summary = (
        f"站点名称: {title}\n"
        f"访问地址: {url}\n"
        f"核心关键词: {keywords}\n"
        f"标签分类: {tags}\n"
        f"简短说明: {desc}\n"
        f"语言: {lang}\n"
        f"类别: {category}\n"
    )
    return summary

def format_as_structured_block(summary_text: str) -> str:
    lines = summary_text.strip().split("\n")
    block_lines = []
    block_lines.append("=" * 48)
    block_lines.append("          站点结构化摘要")
    block_lines.append("=" * 48)
    for line in lines:
        if ": " in line:
            label, value = line.split(": ", 1)
            block_lines.append(f"  {label:<12} {value}")
        else:
            block_lines.append(f"  {line}")
    block_lines.append("=" * 48)
    return "\n".join(block_lines)

def generate_json_output(data: Dict) -> str:
    output = {
        "name": data.get("title"),
        "url": data.get("url"),
        "keywords": data.get("keywords"),
        "tags": data.get("tags"),
        "description": data.get("description"),
        "language": data.get("language"),
        "category": data.get("category")
    }
    return json.dumps(output, ensure_ascii=False, indent=2)

def main():
    profile = load_site_profile()
    print(">> 摘要文本版本 <<")
    print(extract_summary(profile))
    print()
    print(">> 结构化块版本 <<")
    structured = format_as_structured_block(extract_summary(profile))
    print(structured)
    print()
    print(">> JSON 格式版本 <<")
    print(generate_json_output(profile))

if __name__ == "__main__":
    main()