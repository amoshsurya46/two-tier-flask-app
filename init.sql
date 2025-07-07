CREATE TABLE IF NOT EXISTS todos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    priority ENUM('low', 'medium', 'high') DEFAULT 'medium',
    status ENUM('pending', 'completed') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO todos (title, description, priority, status) VALUES 
('Welcome to your Todo App', 'This is your first task. You can edit, complete, or delete it!', 'medium', 'pending'),
('Learn Docker', 'Complete the Docker containerization tutorial', 'high', 'pending'),
('Setup CI/CD Pipeline', 'Configure automated deployment pipeline', 'medium', 'completed');