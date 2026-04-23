def log_stage(stage, content):
    with open("logs/rag_logs.txt", "a", encoding="utf-8") as f:
        f.write(f"\n===== {stage} =====\n")
        f.write(str(content))
        f.write("\n")