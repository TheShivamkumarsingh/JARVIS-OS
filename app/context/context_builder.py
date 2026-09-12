from app.services.memory_service import MemoryService


class ContextBuilder:

    def __init__(self, tool_manager):

        self.memory = MemoryService()
        self.tools = tool_manager

    def build_context(self, user_message: str) -> str:

        profile = self.memory.get_all_profile()
        history = self.memory.get_history()
        tool_descriptions = self.tools.get_tool_descriptions()

        context = "========== USER PROFILE ==========\n"

        if profile:

            for key, value in profile:
                context += f"{key}: {value}\n"

        else:
            context += "No profile information.\n"

        context += "\n========== RECENT CONVERSATION ==========\n"

        if history:

            recent = history[-5:]

            for user, assistant in recent:

                context += f"User: {user}\n"
                context += f"Assistant: {assistant}\n\n"

        else:

            context += "No conversation history.\n"

        context += "\n========== AVAILABLE TOOLS ==========\n"

        if tool_descriptions:
            context += tool_descriptions

        else:
            context += "No tools available.\n"

        context += "\n========== CURRENT MESSAGE ==========\n"

        context += user_message

        return context