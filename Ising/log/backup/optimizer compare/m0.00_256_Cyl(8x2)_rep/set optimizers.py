        self.optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.02)
        self.optimizer = tf.train.AdadeltaOptimizer(learning_rate=2., rho=0.95, epsilon=1e-08,)
        self.optimizer = tf.train.RMSPropOptimizer(learning_rate=0.001, decay=0.99, momentum=0.0, epsilon=1e-10,)
        self.optimizer = tf.train.AdamOptimizer(learning_rate=0.01, beta1=0.8, beta2=0.9999, epsilon=1e-8)
        self.optimizer = tf.train.AdagradOptimizer(learning_rate=0.05)