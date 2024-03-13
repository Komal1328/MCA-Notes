class PrintNumbers {
    private static final Object lock = new Object();
    private static int count = 1;

    static class OddThread extends Thread {
        public void run() {
            while (count < 10) {
                synchronized (lock) {
                    if (count % 2 != 0) {
                        System.out.print(count + " ");
                        count++;
                    }
                }
            }
        }
    }

    static class EvenThread extends Thread {
        public void run() {
            while (count <= 10) {
                synchronized (lock) {
                    if (count % 2 == 0) {
                        System.out.print(count + " ");
                        count++;
                    }
                }
            }
        }
    }

    public static void main(String[] args) {
        Thread oddThread = new OddThread();
        Thread evenThread = new EvenThread();

        oddThread.start();
        evenThread.start();

        try {
            oddThread.join();
            evenThread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
