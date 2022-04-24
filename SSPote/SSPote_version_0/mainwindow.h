#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QProcess>
#include <qpushbutton.h>
#include <QDebug>
#include <QPalette>
#include <QToolButton>
#include <QPushButton>

#include "imagebutton.h"
#include <QObject>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    QPushButton* main_button = nullptr;

public slots:
     void onButtonClicked ();

private:
    Ui::MainWindow *ui;
    bool connected = false;
};
#endif // MAINWINDOW_H
