import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import \
    Features, \
    ConceptsOptions, \
    RelationsOptions, \
    EmotionOptions, \
    EntitiesOptions, \
    SemanticRolesOptions, \
    SentimentOptions

authenticator = IAMAuthenticator('api key')

natural_language_understanding = NaturalLanguageUnderstandingV1(
    authenticator=authenticator,
    version='2018-03-16'
)

natural_language_understanding.set_service_url('stance url')

response = natural_language_understanding.analyze(
  text='Who is the president of Brazil?',
  features=Features(
    concepts=ConceptsOptions(),
    emotion=EmotionOptions(),
    entities=EntitiesOptions(),
    sentiment=SentimentOptions(),
    ))

print(json.dumps(response, indent=2))

response = natural_language_understanding.analyze(
  text='Steve Jobs is the founder of Apple',
  features=Features(
    entities=EntitiesOptions(),
    semantic_roles=SemanticRolesOptions(),
    ))

print(json.dumps(response, indent=2))

response = natural_language_understanding.analyze(
  text='Na FIAP, os alunos são muito dedicados.',
  features=Features(
    relations=RelationsOptions(),
    concepts=ConceptsOptions(),
    emotion=EmotionOptions(),
    entities=EntitiesOptions(),
    semantic_roles=SemanticRolesOptions(),
    sentiment=SentimentOptions(),
    ))

print(json.dumps(response, indent=2))
