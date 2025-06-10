from rilz.client import Client
from rilz.services.databases import Databases
from rilz.query import Query
from rilz.exception import VaultNotFound, VaultValueNotFound

class Vault:
    client:Client
    vault_database_id:str
    vault_database_id:str
    databases = None
    
    def __init__(self, client: Client):
        self.databases  = Databases(client)
        databases = self.databases.list()
        vault_database = next((db for db in databases['databases'] if db['name'] == 'vault'), None)
        if not vault_database:
            databases = Databases(client).create(
                name='vault',
                permission='read-write',
                enabled=True,
            )
            vault_database = databases
        if not vault_database:            
            raise VaultNotFound("Vault database not found. Please create a database named 'vault'.")
        self.vault_database_id = vault_database['$id']
        self.client = client
        
        
    
    def get(self, name: str='config', **kwargs):
        if not self.vault_database_id:
            collections = Databases(self.client).list_collections(self.vault_database_id)
            vault_collection = next((col for col in collections['collections'] if col['name'] == 'vault'), None)
            if not vault_collection:
                vault_collection = Databases(self.client).create_collection(
                    self.vault_database_id,
                    name='vault',
                    permission='read-write',
                    enabled=True,
                )
            self.vault_database_id = vault_collection['$id']
        
        query = Query.equal('name', name)

        collections_exists = self.databases.list_collections(
            self.vault_database_id,            
            queries=[query],
        )
        if not collections_exists['total']:
            raise VaultNotFound(f"Vault collection with name '{name}' not found.")
        collection = collections_exists['collections'][0]
        documents = self.databases.list_documents(
            self.vault_database_id,
            collection['$id'],
            queries=[Query.equal(k, v) for k, v in kwargs.items()] if kwargs else []
        )
        if not documents['total']:
            raise VaultValueNotFound(f"Vault document with name '{name}' and parameters {kwargs} not found.")
        return {k: v for k, v in documents['documents'][0].items() if k != '$id' and k != '$permissions' and k != '$createdAt' and k != '$updatedAt'}
        