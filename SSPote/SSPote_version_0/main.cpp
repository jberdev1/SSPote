#include "mainwindow.h"

#include <QApplication>
#include <QPushButton>
#include <QObject>


void button_pressed(QPushButton b){

}

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    QPushButton activity_button("Appuie sur ce bouton quand tu commence à utiliser la station !", &w);
    activity_button.setGeometry(0, 0, 700, 300);
    w.main_button = &activity_button;
    QObject::connect(&activity_button, SIGNAL(clicked()), &w , SLOT(onButtonClicked()));
    w.show();
    activity_button.show();
    return a.exec();
}
