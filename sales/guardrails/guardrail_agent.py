from agents import Agent, Runner, GuardrailFunctionOutput, input_guardrail
from pydantic import BaseModel

class NameCheckOutput(BaseModel):
  is_name_in_message: bool
  name: str

name_checker_agent = Agent(
  name='Name Checker',
  instructions="Check if the user is including someone's personal name in what they want you to do.",
  output_type=NameCheckOutput,
  model="gpt-4o-mini"
)


@input_guardrail
async def guardrail_against_name(ctx, agent, message):
    result = await Runner.run(name_checker_agent, message, context=ctx.context)
    is_name_in_message = result.final_output.is_name_in_message
    return GuardrailFunctionOutput(output_info={"found_name": result.final_output}, tripwire_triggered=is_name_in_message)