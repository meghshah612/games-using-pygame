from .config import SCORES_FILE


def _ensure_scores_file():
    if not SCORES_FILE.exists():
        SCORES_FILE.write_text("0")


def max_score() -> int:
    _ensure_scores_file()

    try:
        return int(SCORES_FILE.read_text().strip() or 0)
    except ValueError:
        return 0


def update_score(new_score: int) -> None:
    if new_score > max_score():
        SCORES_FILE.write_text(str(new_score))
