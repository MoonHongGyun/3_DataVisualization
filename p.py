            max = b[0]
            min = b[0]
            sum = 0
            aver = 0
            Aver = 0
            for i in range(b_len):
                if b[i] > max:
                    max = b[i]

            for i in range(b_len):
                if b[i] < min:
                    min = b[i]

            for i in range(b_len):
                sum += b[i]

            aver = sum / b_len

            Aver = aver * 1.1
            aver = math.trunc(aver)
            Aver = math.trunc(Aver)

            self.max_label.setText(f'최대 금액: {max}원 / 최소 금액: {min}원 / 평균 금액: {aver}원 / 예상 평균 금액: {Aver}원')

            #for draw graph
            self.fig = plt.Figure()
            self.canvas = FigureCanvas(self.fig)
            self.verticalLayout.addWidget(self.canvas)

            x = np.arange(b_len)
            y = b

            ax = self.fig.add_subplot(111)
            ax.plot(x, y,color = 'Peru')
            ax.set_xlabel('daily')
            ax.set_ylabel('won')

            ax.legend()
            self.canvas.draw()

if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindow = Windowclass()
    myWindow.show()
    app.exec_()
