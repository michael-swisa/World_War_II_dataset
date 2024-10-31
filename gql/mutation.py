from graphene import ObjectType
from gql.mutations.mission_mutations import MissionInput


class Mutation(ObjectType):
    add_mission = MissionInput.Field()
