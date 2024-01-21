from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app import Expense  # Asegúrate de importar tu modelo Expense

# Configura el motor para conectarse a la base de datos SQLite
engine = create_engine('sqlite:///instance/expenses.db')

# Crea una sesión de SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

# Ejemplo de consulta para obtener todos los gastos para un concepto y mes específicos
concept_name = 'Auto fuel'
month_name = 'January'

expenses = session.query(Expense).filter_by(concept=concept_name, month=month_name).all()

# Imprime los resultados
for expense in expenses:
    print(f"Concept: {expense.concept}, Month: {expense.month}, Amount: {expense.amount}, Notes: {expense.notes}")

# Cierra la sesión
session.close()
