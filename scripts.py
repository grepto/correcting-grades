import random
import datetime

from datacenter.models import Schoolkid, Mark, Сhastisement, Commendation, Lesson


def get_schoolkid(name):
    return Schoolkid.objects.filter(full_name__contains=name)[0]

def fix_marks(schoolkid):
    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for mark in marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    Сhastisement.objects.filter(schoolkid=schoolkid).delete()


def add_commendation(schoolkid, subject_name)
    commendations = ['Молодец!',
                     'Отлично!',
                     'Хорошо!',
                     'Гораздо лучше, чем я ожидал!',
                     'Ты меня приятно удивил!',
                     'Великолепно!',
                     'Прекрасно!',
                     'Ты меня очень обрадовал!',
                     'Именно этого я давно ждал от тебя!',
                     'Сказано здорово – просто и ясно!',
                     'Ты, как всегда, точен!',
                     'Очень хороший ответ!',
                     'Талантливо!',
                     'Ты сегодня прыгнул выше головы!',
                     'Я поражен!',
                     'Уже существенно лучше!',
                     'Потрясающе!',
                     'Замечательно!',
                     'Прекрасное начало!',
                     'Так держать!',
                     'Ты на верном пути!',
                     'Здорово!',
                     'Это как раз то, что нужно!',
                     'Я тобой горжусь!',
                     'С каждым разом у тебя получается всё лучше!',
                     'Мы с тобой не зря поработали!',
                     'Я вижу, как ты стараешься!',
                     'Ты растешь над собой!',
                     'Ты многое сделал, я это вижу!',
                     'Теперь у тебя точно все получится!', ]
    lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter,
                                   subject__title__contains=subject_name)[0]
    Commendation.objects.create(text=random.choice(commendations), created=datetime.date.today(), schoolkid=schoolkid,
                                subject=lesson.subject, teacher=lesson.teacher)


def main():
    schoolkid = get_schoolkid('Фролов Иван')
    print(schoolkid)


if __name__ == '__main__':
    main()
