# Sistema Bancário

Este sistema bancário permite realizar operações simples de depósito, saque e extrato para um único usuário.

## Funcionalidades

- **Depositar**: Permite depositar valores positivos na conta.
- **Sacar**: Permite realizar até 3 saques diários, com um limite de R$ 500,00 por saque.
  - Saques podem ser reduzidos em 50% em finais de semana ou após as 20 horas.
- **Extrato**: Exibe todos os depósitos e saques realizados, além do saldo atual.

## Regras

1. **Depósito**:
   - Valores devem ser positivos.
   - Todos os depósitos são armazenados e exibidos no extrato.

2. **Saque**:
   - Limite de R$ 500,00 por saque.
   - Máximo de 3 saques por dia.
   - Se não houver saldo suficiente, uma mensagem de erro é exibida.
   - Em finais de semana ou após as 20 horas, o limite de saque é reduzido em 50%.

3. **Extrato**:
   - Lista todos os depósitos e saques.
   - Se não houver movimentações, exibe "Não foram realizadas movimentações".

## Como Utilizar

1. Execute o código.
2. Escolha a opção desejada no menu.
3. Siga as instruções na tela para realizar as operações.
