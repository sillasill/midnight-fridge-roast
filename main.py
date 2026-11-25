import os

ROAST = "My fridge locks at midnight to look after me, which is touching — except its whole job is keeping the ice cream frozen."

def main():
    if not 1 <= len(ROAST) <= 200:
        raise ValueError("roast must be 1 to 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ROAST)

if __name__ == "__main__":
    main()
