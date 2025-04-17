from django.db import models
"""class Paciente(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    nome_completo = models.CharField(max_length=150)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    
    convenio = models.ForeignKey('Convenio', on_delete=models.SET_NULL, null=True, blank=True) # referenciado para que possamos depois cadastrar os convênios e associar.
    numero_carteira = models.CharField(max_length=30, blank=True, null=True) #número do plano de saúde (caso tenha).

    historico_medico = models.TextField(blank=True, null=True) #campo livre para observações médicas relevantes.

    criado_em = models.DateTimeField(auto_now_add=True) #para controle de alterações.
    atualizado_em = models.DateTimeField(auto_now=True) #para controle de alterações.

    def __str__(self):
        return self.nome_completo


class Convenio(models.Model):
    nome = models.CharField(max_length=100, unique=True) #nome: nome do plano ou convênio (ex: Unimed, Bradesco Saúde etc.).
    cnpj = models.CharField(max_length=18, blank=True, null=True) #cnpj: caso queira registrar o número do convênio.
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True) #campo aberto para anotações diversas (cobertura, limites, etc.).

    ativo = models.BooleanField(default=True) #usado para desativar convênios sem apagar do sistema.

    criado_em = models.DateTimeField(auto_now_add=True) #timestamps de controle.
    atualizado_em = models.DateTimeField(auto_now=True) #timestamps de controle.

    def __str__(self):
        return self.nome
"""