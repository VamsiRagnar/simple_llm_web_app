from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.sequential import SequentialChain
from langchain.chains.llm import LLMChain
from keys import openapi_key
import os
os.environ['OPENAI_API_KEY'] = openapi_key

llm = ChatOpenAI(model_name="gpt-3.5-turbo-instruct",temperature=0.5)

def generate_player_names(year: str,sport:str,nationality:str) -> list[str]:
   

    prompt_template_name = PromptTemplate(
        input_variables=['year','sport','nationality'],
        template="""Please provide the list of players in {sport} team of {nationality} during the year {year}. 
                    Provide the names such that they should not exceed the actual team count.
                    Example cricket team has total of 15 players.
                    Return it as a comma separated list """
                )

    name_chain = LLMChain(llm=llm,
                          prompt=prompt_template_name,
                          output_key='player_names')

    chain = SequentialChain(
        chains=[name_chain],
        input_variables=['year','sport','nationality'],
        output_variables=['player_names']
    )

    response = chain({'year': year,
                      'sport': sport,
                      'nationality': nationality})
    return response

