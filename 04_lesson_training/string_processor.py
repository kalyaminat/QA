class StringProcessor:
    @staticmethod
    def process(text: str) -> str:
        if not text:
            return "."
        processed_text = text[0].upper() + text[1:]
        if not processed_text.endswith("."):
            processed_text += "."
        return processed_text