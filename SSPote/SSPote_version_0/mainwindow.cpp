#include "mainwindow.h"
#include "ui_mainwindow.h"


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    main_button = new QPushButton(nullptr);
    main_button->setText("Appuie sur ce bouton quand tu commence à utiliser la station !");
    setGeometry(0, 0, 635, 300);
    setCentralWidget(main_button);
    setWindowTitle("SSPote");

    QPixmap button_back("../res/button_back.png");
    QIcon ButtonIcon(button_back);

    main_button->setStyleSheet("background-image: url('../res/button_back.png'); color: white;");
    QObject::connect(main_button, SIGNAL(clicked()), this , SLOT(onButtonClicked()));

}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::onButtonClicked()
{
    qDebug () << "Button clicked";
    QProcess process;
    QString scriptFile =  QCoreApplication::applicationDirPath() + "/../../../SSPote_bot/SSPote_bot.py";
    qDebug() << scriptFile;

    if(connected){
      main_button->setText("Appuie sur ce bouton quand tu commence à utiliser la station !");
      //process.execute("python3", {scriptFile, "disconnected"});

    }else{
      main_button->setText("Appuie sur ce bouton quand tu as fini d'utiliser la station !");
      //process.execute("python3", {scriptFile, "connected"});
    }
     connected = !connected;

}
