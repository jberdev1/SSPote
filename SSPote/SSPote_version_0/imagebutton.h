#ifndef IMAGEBUTTON_H
#define IMAGEBUTTON_H

#include <QAbstractButton>
#include <QObject>
#include <QPainter>
#include <QWidget>

class ImageButton : public QAbstractButton
{
QPixmap m_pixmap;

public:
    ImageButton(const QString &image_path, const QString &text, QWidget *parent = nullptr);
    ImageButton(const QString &text, QWidget *parent = nullptr);
    ImageButton(QWidget *parent = nullptr);
    void setPixmap( const QPixmap& pm ) { m_pixmap = pm; update(); }
        QSize sizeHint() const { return m_pixmap.size(); }
protected:
    void paintEvent( QPaintEvent* e ) {
        QPainter p( this );
        p.drawPixmap( 0, 0, m_pixmap );
    }
};

#endif // IMAGEBUTTON_H
