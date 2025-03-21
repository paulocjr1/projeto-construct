from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    available_permissions = {
        'cadastrar_produtos': True,
        'liberar_desconstos': True,
        'cadastrar_vendedor': True,
    }

class Vendedor(AbstractUserRole):
    available_permissions = {
        'realizar_venda': True
    }