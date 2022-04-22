#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QProcess>
#include <qpushbutton.h>

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
     void onButtonClicked () {
         qDebug () << "Button clicked";
         if(connected){
            main_button->setText("Appuie sur ce bouton quand tu commence à utiliser la station !");
            qDebug() << QProcess::execute("py ../../SSPote_bot.py connected");
         }
         else{
            main_button->setText("Appuie sur ce bouton quand tu as terminé d'utiliser la station !");
            qDebug() << QProcess::execute("py ../../SSPote_bot.py disconnected");
         }
         connected = !connected;

     };

private:
    Ui::MainWindow *ui;
    bool connected = false;
};
#endif // MAINWINDOW_H
