#include "imagebutton.h"



ImageButton::ImageButton(const QString &image_path, const QString &text, QWidget *parent)
{
    m_pixmap = QPixmap(image_path);
    this->setText(text);
    this->setParent(parent);
}

ImageButton::ImageButton(const QString &text, QWidget *parent)
{
    this->setText(text);
    this->setParent(parent);
}

ImageButton::ImageButton(QWidget *parent)
{
    this->setParent(parent);
}
