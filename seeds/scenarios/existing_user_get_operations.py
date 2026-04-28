from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan, SeedOperationsPlan


class ExistingUserGetOperationsSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для существующего пользователя, который просматривает информацию об операциях по кредитному счету.
    Создаём 300 пользователей, каждому из которых открывается один кредитный счёт.
    По кредитному счету выполняется 5 операций покупки, 1 операция пополнения счёта, 1 операция снятия наличных.
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        Возвращает план сидинга для создания пользователей и их счетов.
        Мы создаём 300 пользователей, каждый получит кредитный счёт.
        На каждый счет создадутся 5 операций покупки, 1 операция пополнения счёта, 1 операция снятия наличных.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,  # Создаём 300 пользователей
                credit_card_accounts=SeedAccountsPlan(
                    count=1,
                    purchase_operations=SeedOperationsPlan(count=5),  # операция покупки 5шт
                    cash_withdrawal_operations=SeedOperationsPlan(count=1), # операция снятия наличных
                    top_up_operations=SeedOperationsPlan(count=1) # операция пополнения
                )  # кредитный счёт на пользователя
            ),
        )

    @property
    def scenario(self) -> str:
        """
        Возвращает название сценария сидинга.
        Это имя будет использоваться для сохранения данных сидинга.
        """
        return "existing_user_get_operations"


if __name__ == '__main__':
    """
    Запуск сценария сидинга вручную.
    Создаём объект сценария и вызываем метод build для создания данных.
    """
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()  # Запуск сидинга
