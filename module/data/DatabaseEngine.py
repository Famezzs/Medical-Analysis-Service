from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from module.static.Configuration import Configuration

# Class which is used for providing CRUD operations over all entity records
class DatabaseEngine:
    def __init__(self, configuration: Configuration):
        self.engine = create_engine(configuration.database_configuration.connection_string)
        self.session = sessionmaker(bind=self.engine)
        self.printer = configuration.database_configuration.printer
        self.create_all_tables(configuration.database_configuration.entities)

    def create_all_tables(self, entities):
        for entity in entities:
            entity.metadata.create_all(self.engine)

    def add_record(self, record):
        session = self.session()
        try:
            session.add(record)
            session.flush()
            record_id = record.id
            session.commit()
            return record_id 
        except SQLAlchemyError as e:
            session.rollback()
            self.printer.print(f"Error adding record: {e}", True)
            return False
        finally:
            session.close()

    def query_records(self, model, filter_condition=None):
        session = self.session()
        try:
            return session.query(model).filter(filter_condition).all()
        except SQLAlchemyError as e:
            self.printer.print(f"Error querying records: {e}", True)
            return []
        finally:
            session.close()

    def update_record(self, model, filter_condition, update_values):
        session = self.session()
        try:
            session.query(model).filter(filter_condition).update(update_values)
            session.commit()
            return True
        except SQLAlchemyError as e:
            session.rollback()
            self.printer.print(f"Error updating record: {e}", True)
            return False
        finally:
            session.close()

    def delete_record(self, model, filter_condition):
        session = self.session()
        try:
            session.query(model).filter(filter_condition).delete()
            session.commit()
            return True
        except SQLAlchemyError as e:
            session.rollback()
            self.printer.print(f"Error deleting record: {e}", True)
            return False
        finally:
            session.close()