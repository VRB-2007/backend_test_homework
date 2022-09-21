

class Training: #Базовый класс Training

    M_IN_KM = 1000
    LEN_STEP, LEN_STEP_SW = 0.65, 1.38

    
    def __init__(self, action: int, duration: float,  weight: float,): #Конструктор каждого из классов должен получать информацию с датчиков
        self.action = action
        self.duration = duration
        self.weight = weight
 

    def get_distance(self): #возвращает дистанцию (в километрах), которую преодолел пользователь за время тренировки.
        if self == "SWM":
            LEN_STEP = 1.38
        else:
            LEN_STEP = 0.65
        
        return self.action * self.LEN_STEP / self.M_IN_KM


    def get_mean_speed(self): #возвращает значение средней скорости движения во время тренировки.

        return Training.get_distance(self) / self.duration


    def get_spent_calories(self): # возвращает количество килокалорий, израсходованных за время тренировки.
        pass


   # def show_training_info(): #возвращает объект класса сообщения.



class Running(Training): #реализации классов-наследников class Running
 

    def get_spent_calories(self): #Расчёт калорий для этого класса
        coeff_calorie_1, coeff_calorie_2 = 18, 20  
        spent_calories_0 = coeff_calorie_1 * super().get_mean_speed(self) 
        spent_calories = (spent_calories_0 - coeff_calorie_2) * self.weight / self.M_IN_KM * self.duration / self.MIN
        return spent_calories



class SportsWalking(Training): #реализации классов-наследников class SportsWalking
 

    def __init__(self,  action: int,  duration: float,  weight: float,  height: float):
        
        self.action = action
        self.duration = duration
        self.weight = weight
        self.height = height


    def get_spent_calories(self): #Расчёт калорий для этого класса
        
        coeff_calorie_1 = 0.035
        coeff_calorie_2 = 0.029
        spent_calorie0 = (super().get_mean_speed(self) ** 2 // self.height)
        spent_calories  = ((coeff_calorie_1 * self.weight) + spent_calorie0 * coeff_calorie_2 * self.weight) * self.duration / self.MIN
        return spent_calories

    

class Swimming(Training): #реализации классов-наследников class Swimming
 

    def __init__(self, action: int,  duration: float,  weight: float, length_pool: float, count_pool: float):

        self.action = action
        self.duration = duration
        self.weight = weight
        self.length_pool = length_pool
        self.count_pool = count_pool


    def get_mean_speed(self): #возвращает значение средней скорости class Swimming

        mean_speed = self.length_pool * self.count_pool / self.M_IN_KM / self.duration
        return mean_speed


    def get_spent_calories(self): #Расчёт калорий для этого класса
        coeff_calorie_1, coeff_calorie_2 = 1.1, 2  
        spent_calories = (self.get_mean_speed(self) + coeff_calorie_1) * coeff_calorie_2 * self.weight
        return spent_calories
 


class InfoMessage: #класс для создания объектов сообщений


    def __init__(self, training_type: str, duration: float, distance: float, speed: float, calories: float):

        self.duration = duration
        # training_type
        self.training_type = training_type
        self.distance = training_type.get_distance
        self.speed = training_type.get_mean_speed
        self.calories = training_type.get_spent_calories


    def get_message(self): # возвращает строку сообщения:

        print(f'Тип тренировки: {self.training_type}'
              f'Длительность: {self.duration}:.3f ч.'
              f'Дистанция: {self.distance}:.3f км'
              f'Ср. скорость: {self.speed}:.3f км / ч'
              f'Потрачено ккал: {self.calories}.')


def main(training: Training): #должна принимать на вход экземпляр класса Training

    info = training.show_training_info()
    infoprint = info.get_message()
    print(infoprint)



def read_package(workout_type: str, data: list): #принимает на вход код тренировки и список её параметров.

    Action = {
        'SWM': 'Swimming',
        'RUN': 'Running',
        'WLK': 'SportsWalking'
    }

    training = read_package(workout_type, data)
    main(training) 


if __name__ == '__main__':

    packages = [        
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]
    
    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training) 

