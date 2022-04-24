#include "mainwindow.h"

#include <QApplication>



int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    //specify a new font.
    QFont newFont("Segoe UI Semibold", 16, QFont::Normal, false);
    //set font of application
    QApplication::setFont(newFont);
    MainWindow w;
    w.show();
    return a.exec();
}
