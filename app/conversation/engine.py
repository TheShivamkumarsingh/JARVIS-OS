from app.brain.memory_extractor import MemoryExtractor
from app.context.context_builder import ContextBuilder
from app.services.memory_service import MemoryService
from app.tools.tool_manager import ToolManager
from app.brain.brain import Brain


class ConversationEngine:

    def __init__(self):

        self.extractor = MemoryExtractor()
        self.memory = MemoryService()
        self.context = ContextBuilder()
        self.tools = ToolManager()
        self.brain = Brain()

    def process(self, user_message: str):

        # -----------------------------
        # 1. Extract Profile Memory
        # -----------------------------

        extracted = self.extractor.extract(user_message)

        if extracted:

            self.memory.save_profile(
                extracted["key"],
                extracted["value"]
            )

        # -----------------------------
        # 2. Tool Execution
        # -----------------------------

        tool_result = self.tools.execute(user_message)

        if tool_result is not None:

            assistant_message = tool_result

            self.memory.remember(
                user_message,
                assistant_message
            )

            return assistant_message

        # -----------------------------
        # 3. Build Context
        # -----------------------------

        context = self.context.build_context(
            user_message
        )

        # -----------------------------
        # 4. Brain
        # -----------------------------

        assistant_message = self.brain.think(context)

        # -----------------------------
        # 5. Save Conversation
        # -----------------------------

        self.memory.remember(
            user_message,
            assistant_message
        )

        return assistant_message