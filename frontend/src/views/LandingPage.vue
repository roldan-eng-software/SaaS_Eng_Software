<template>
  <div class="d-flex flex-column min-vh-100 bg-light text-dark">
    <!-- Header -->
    <header class="sticky-top bg-light bg-opacity-90 border-bottom border-secondary border-opacity-25" style="backdrop-filter: blur(8px); z-index: 1050;">
      <div class="container-fluid" style="max-width: 1200px;">
        <nav class="navbar navbar-expand-lg navbar-light py-3">
          <div class="container-fluid px-0">
            <a class="navbar-brand d-flex align-items-center gap-2" href="#">
              <img src="/src/views/Logotipo.png" alt="Roldan Eng Software Logo" style="width: 36px; height: 36px; object-fit: contain;">
              <h2 class="mb-0 fw-bold fs-5">Roldan Eng Software</h2>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
              <ul class="navbar-nav ms-auto me-3">
                <li class="nav-item"><a class="nav-link" href="#inicio" style="color: #0052CC;">Início</a></li>
                <li class="nav-item"><a class="nav-link" href="#sobre" style="color: #0052CC;">Sobre Nós</a></li>
                <li class="nav-item"><a class="nav-link" href="#servicos" style="color: #0052CC;">Serviços</a></li>
                <li class="nav-item"><a class="nav-link" href="#portfolio" style="color: #0052CC;">Portfólio</a></li>
                <li class="nav-item"><a class="nav-link" href="#contato" style="color: #0052CC;">Contato</a></li>
              </ul>
              <div class="d-flex gap-2">
                <router-link to="/login" class="btn btn-outline-info px-3" style="border-color: #008B8B; color: #008B8B;">
                  Login
                </router-link>
                <button class="btn text-white px-3 d-none d-sm-block" style="background-color: #008B8B;">
                  Solicitar Orçamento
                </button>
              </div>
            </div>
          </div>
        </nav>
      </div>
    </header>

    <!-- Main Content -->
    <main class="flex-grow-1">
      <!-- Hero Section -->
      <section id="inicio" class="py-5 text-white" style="background-color: #0052CC;">
        <div class="container" style="max-width: 1200px;">
          <div class="row align-items-center g-5 py-md-5">
            <div class="col-md-6 text-center text-md-start">
              <h1 class="display-3 fw-black mb-4">Roldan Eng Software</h1>
              <p class="lead mb-4 text-white-50">
                Transformando suas ideias em soluções digitais inovadoras para impulsionar o seu negócio.
              </p>
              <button class="btn btn-lg text-white mt-3" style="background-color: #008B8B;">
                Conheça Nossos Serviços
              </button>
            </div>
            <div class="col-md-6">
              <div class="ratio ratio-16x9 rounded-3" style='background-image: url("/web-dev-hero.png"); background-size: cover; background-position: center;'></div>
            </div>
          </div>
        </div>
      </section>

      <!-- Services Section -->
      <section id="servicos" class="py-5 bg-light">
        <div class="container" style="max-width: 1200px;">
          <div class="text-center mb-5">
            <h2 class="display-5 fw-bold mb-3">Nossas Soluções para o seu Negócio</h2>
            <p class="lead text-muted">Oferecemos serviços completos para alavancar sua presença digital e otimizar sua gestão.</p>
          </div>
          <div class="row g-4">
            <div class="col-md-6">
              <div class="card h-100 border-secondary border-opacity-25">
                <div class="card-body p-4">
                  <span class="material-symbols-outlined fs-1 mb-3" style="color: #4A6FA5;">campaign</span>
                  <h3 class="card-title h4 fw-bold mb-3">Marketing Web</h3>
                  <p class="card-text text-muted">
                    Desenvolvemos sites otimizados para SEO e criamos estratégias digitais que aumentam sua presença online e geram leads qualificados.
                  </p>
                  <a href="#" class="text-decoration-none fw-semibold d-inline-flex align-items-center gap-1" style="color: #4A6FA5;">
                    Saiba Mais
                    <span class="material-symbols-outlined">arrow_forward</span>
                  </a>
                </div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="card h-100 border-secondary border-opacity-25">
                <div class="card-body p-4">
                  <span class="material-symbols-outlined fs-1 mb-3" style="color: #4A6FA5;">monitoring</span>
                  <h3 class="card-title h4 fw-bold mb-3">Sistemas de Gestão Financeira</h3>
                  <p class="card-text text-muted">
                    Construímos dashboards financeiros e sistemas ERP customizados para um controle preciso e tomada de decisões estratégicas para seu negócio.
                  </p>
                  <a href="#" class="text-decoration-none fw-semibold d-inline-flex align-items-center gap-1" style="color: #4A6FA5;">
                    Saiba Mais
                    <span class="material-symbols-outlined">arrow_forward</span>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- About Section -->
      <section id="sobre" class="py-5 text-white" style="background-color: #4A6FA5;">
        <div class="container" style="max-width: 1200px;">
          <div class="row g-5 align-items-center">
            <div class="col-lg-6">
              <h2 class="display-5 fw-bold mb-4">Sobre a Roldan Eng Software</h2>
              <p class="mb-4">Somos uma equipe apaixonada por tecnologia e inovação, dedicada a criar soluções de software que não apenas atendem, mas superam as expectativas de nossos clientes. Desde nossa fundação, temos o compromisso de transformar ideias complexas em sistemas intuitivos e eficientes.</p>
              <div class="row g-3">
                <div class="col-md-6">
                  <div class="card bg-white bg-opacity-10 border-white border-opacity-20 text-white p-3">
                    <span class="material-symbols-outlined fs-1 mb-2">rocket</span>
                    <h3 class="h5 fw-bold mb-2">Missão</h3>
                    <p class="small mb-0">Impulsionar o sucesso de nossos clientes através de soluções de software personalizadas, inovadoras e de alta qualidade.</p>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="card bg-white bg-opacity-10 border-white border-opacity-20 text-white p-3">
                    <span class="material-symbols-outlined fs-1 mb-2">visibility</span>
                    <h3 class="h5 fw-bold mb-2">Visão</h3>
                    <p class="small mb-0">Ser referência no desenvolvimento de software, reconhecida pela excelência técnica e pelo impacto positivo nos negócios de nossos parceiros.</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-lg-6">
              <h3 class="h3 fw-bold mb-4">Nossa Equipe</h3>
              <div class="row g-4 text-center">
                <div class="col-4">
                  <div class="rounded-circle mx-auto mb-3" style='width: 96px; height: 96px; background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuCYcssKZhuXa22fuWvKmy6l3aM0DQ2VA0mhixLaBkbZY6T3Fko5dL8XGjevr-2ApY5fMG1rLmjqcwb3G80aqgSnS5scS1G55bn1Xu1kbUdjfF-LTnTpKqkRc6G5DdXNJVJrJyx7-p2y9-UuczIXezcTwWMTN42-3blnUqGbI3-2_-zrp6ZFeZtBUXzgvOQi0gEEOMT5Rr31hK2asoHisQLrOjdyO_reJJ20nV6VaJBLu4WyUJWeJ6bsYQngYxfNcvaPB_tdeB5deqw"); background-size: cover; background-position: center;'></div>
                  <p class="fw-bold mb-1">Carlos Roldan</p>
                  <p class="small text-white-50 mb-0">CEO & Fundador</p>
                </div>
                <div class="col-4">
                  <div class="rounded-circle mx-auto mb-3" style='width: 96px; height: 96px; background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuCCGi0Ig_iX980I2brhL4XkVW1VxDMM30BzrKW2M_P2YoLdVqO_3Ajn7nxv2LisYEL39URhaJriztdb1X47Aix8btykgsUJjF2MKQ1SXDb0ild43rDvV0ljlQrzqB_3zuRV51yFJBSQpwiFfF7ZcPS0mnnJpOb8d3ep36aA3xf8lBQVynOIUrKfb6gVs425fja-tVitzRpl7cHHicKQlQXpwbLht-ivCqqJ558adLuZqL_rI1aBvwH_GIkgK8sQMw98jTtC7Vl936s"); background-size: cover; background-position: center;'></div>
                  <p class="fw-bold mb-1">Ana Pereira</p>
                  <p class="small text-white-50 mb-0">Gerente de Projetos</p>
                </div>
                <div class="col-4">
                  <div class="rounded-circle mx-auto mb-3" style='width: 96px; height: 96px; background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuA7oIDkO4ujGrIlYeQZBVYoGHxjoNhTs_CQ1_sY4EtnUfbLdg7iqyLKNuROXU5MD4cxXRz1NTtRVxMncUkQkogCXbYLpy569Ed_T8TJeoQFzoq_91XmV1qP5096dgfKHSB2GG9SZ7fVVyzw8OprpMlIJ9AKQFLUqVUBmcoRLNgwzgHw8PUwf11dGRN0ze9Ip11GetbPutj5pGuq0WNemJzmc5i-F4yr5znYlNzoiJkRWstxISoojf3vlXk7_BSny1it3SpuJYHxtMs"); background-size: cover; background-position: center;'></div>
                  <p class="fw-bold mb-1">Lucas Martins</p>
                  <p class="small text-white-50 mb-0">Engenheiro de Software Sênior</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Projects Section -->
      <section id="portfolio" class="py-5 bg-light">
        <div class="container" style="max-width: 1200px;">
          <div class="text-center mb-5">
            <h2 class="display-5 fw-bold mb-3">Projetos de Sucesso</h2>
            <p class="lead text-muted">Confira alguns dos projetos que tivemos o prazer de desenvolver.</p>
          </div>
          <div class="row g-4">
            <div class="col-lg-4 col-md-6">
              <div class="card h-100 border-secondary border-opacity-25">
                <div class="ratio ratio-16x9" style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuBBp5gPlVRI8LMG2Q0ToGSLLYhvx15vmjffM7MlOjEpukQQAxu4hlDWf8oY7VeRYd2Fejl7KtdMrcld7dn84HyQS4ks4bmGNSKzlr-423KjtUzzpm_ru319TqU2B4dfa_ADM6JNre5hIVKN_0cUdo_6BBG3jEMt_sqIwbMCIBf5r0967U1deF34OqFl0ToZs2nnTMS7ORLepRY8SxuBwWjBZVwYLy_EwLTo5TykXCoVJmzpODfnsY9yZc4RiqtM3ivcPah2Gj6K6M8"); background-size: cover; background-position: center;'></div>
                <div class="card-body p-4">
                  <h3 class="h5 fw-bold mb-2">Sistema de Gestão Financeira</h3>
                  <p class="card-text text-muted small">Dashboard completo para análise de métricas financeiras, com relatórios customizáveis e interface intuitiva.</p>
                  <div class="d-flex flex-wrap gap-2 mt-3">
                    <span class="badge rounded-pill" style="background-color: rgba(74, 111, 165, 0.1); color: #4A6FA5;">ERP</span>
                    <span class="badge rounded-pill" style="background-color: rgba(74, 111, 165, 0.1); color: #4A6FA5;">Dashboard</span>
                    <span class="badge rounded-pill" style="background-color: rgba(74, 111, 165, 0.1); color: #4A6FA5;">Finanças</span>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-lg-4 col-md-6">
              <div class="card h-100 border-secondary border-opacity-25">
                <div class="ratio ratio-16x9" style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuCwhaKiYY6681EvCiGB2NuE8A55vsAUb_W08twdlKLKcoFQCtiWfKGV6q7cLmDDc303ruoqdKRiBH6aogi9NX5QW2txuSrVKjYtK52ki2T6vclkyzWfdnIr1uZcCpea_q0pISGPhsi38wbVABPmNBPXDJUayZFxG3dghCFSjU6PMGBSARAiwria4OcJFptehzWxNqRu1B1qmnesMgSW_vrPt9aIFFMf7o2vugDAL4DM0ooldvRiZJCRvScVaG-qUydNSnnhW0EmgTw"); background-size: cover; background-position: center;'></div>
                <div class="card-body p-4">
                  <h3 class="h5 fw-bold mb-2">Website Institucional & SEO</h3>
                  <p class="card-text text-muted small">Criação de um site responsivo e otimizado para motores de busca, aumentando a visibilidade e captação de clientes.</p>
                  <div class="d-flex flex-wrap gap-2 mt-3">
                    <span class="badge rounded-pill" style="background-color: rgba(74, 111, 165, 0.1); color: #4A6FA5;">Web Design</span>
                    <span class="badge rounded-pill" style="background-color: rgba(74, 111, 165, 0.1); color: #4A6FA5;">SEO</span>
                    <span class="badge rounded-pill" style="background-color: rgba(74, 111, 165, 0.1); color: #4A6FA5;">Marketing</span>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-lg-4 col-md-6">
              <div class="card h-100 border-secondary border-opacity-25">
                <div class="ratio ratio-16x9" style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuDlI7hFShyRETwmEZ2PmULd0Y1xSWQc9xzpePk2Offjv_0ubd8wzFe6naRtxJwPGZWxWL-Zn_jmaJ-BsN1lfjZPYFmzl2epO1VaSy-PDlaxqAZlTUy0xgnsO2pu2NhxzTwnn0d3CkWTaIm_3PMRr3IZnLHFUvhKqbaWRzm6z0pcHah3eXuWsvNCNt10Kx44SPO1-gkbenvmQ6Sj5k11RJMKuy3aU6K7Fxo3w0eb7tPON4fdovOLD8NLL7O_OkvDChTn31Q1e2Hr42M"); background-size: cover; background-position: center;'></div>
                <div class="card-body p-4">
                  <h3 class="h5 fw-bold mb-2">Plataforma E-commerce</h3>
                  <p class="card-text text-muted small">Solução de e-commerce completa, com integração de pagamentos, gestão de estoque e design focado na conversão.</p>
                  <div class="d-flex flex-wrap gap-2 mt-3">
                    <span class="badge rounded-pill" style="background-color: rgba(74, 111, 165, 0.1); color: #4A6FA5;">E-commerce</span>
                    <span class="badge rounded-pill" style="background-color: rgba(74, 111, 165, 0.1); color: #4A6FA5;">UX/UI</span>
                    <span class="badge rounded-pill" style="background-color: rgba(74, 111, 165, 0.1); color: #4A6FA5;">Vendas</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Testimonials Section -->
      <section class="py-5">
        <div class="container" style="max-width: 1200px;">
          <div class="text-center mb-5">
            <h2 class="display-5 fw-bold mb-3">O Que Nossos Clientes Dizem</h2>
            <p class="lead text-muted">A satisfação de nossos clientes é a nossa maior recompensa.</p>
          </div>
          <div class="row g-4">
            <div class="col-lg-4 col-md-6">
              <div class="card h-100 border-secondary border-opacity-25">
                <div class="card-body p-4 d-flex flex-column">
                  <div class="mb-3 text-warning">
                    <span class="material-symbols-outlined">star</span>
                    <span class="material-symbols-outlined">star</span>
                    <span class="material-symbols-outlined">star</span>
                    <span class="material-symbols-outlined">star</span>
                    <span class="material-symbols-outlined">star</span>
                  </div>
                  <p class="text-muted fst-italic flex-grow-1">"A Roldan Eng Software transformou nosso sistema de gestão. A equipe é incrivelmente profissional e entregou um produto que superou todas as nossas expectativas."</p>
                  <div class="d-flex align-items-center gap-3 mt-3">
                    <div class="rounded-circle" style='width: 48px; height: 48px; background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuCIYS-wf3dRTdZrKoVhdEsyJWG4lhNyWRcQc8eChY7d9__9kOocvl7O-TSqVzuNfaGv0NGT1ZMZiMWnL80s5o6-pk4bZKymuykb6BqZNbCZGa95_USObbnaHxCo2ZcdQmScvD-EjWzylqKQPWS24fZal7FhFcdLfK5AfUESGpvGr7aUhsGe_Pu3XEq6HwIh0wWds7_I0FBHlMVhl5HkPJf0wEXMKM7kPEMFmZ8uUWRniIVNzoV8Cnm0hLDM6PywrHnvIY-o28Fwwiw"); background-size: cover; background-position: center;'></div>
                    <div>
                      <p class="fw-bold mb-0">João Silva</p>
                      <p class="small text-muted mb-0">CEO, InovaTech</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-lg-4 col-md-6">
              <div class="card h-100 border-secondary border-opacity-25">
                <div class="card-body p-4 d-flex flex-column">
                  <div class="mb-3 text-warning">
                    <span class="material-symbols-outlined">star</span>
                    <span class="material-symbols-outlined">star</span>
                    <span class="material-symbols-outlined">star</span>
                    <span class="material-symbols-outlined">star</span>
                    <span class="material-symbols-outlined">star</span>
                  </div>
                  <p class="text-muted fst-italic flex-grow-1">"O trabalho de marketing web e SEO foi impecável. Vimos um aumento significativo no tráfego orgânico e na geração de leads em poucos meses. Recomendo fortemente!"</p>
                  <div class="d-flex align-items-center gap-3 mt-3">
                    <div class="rounded-circle" style='width: 48px; height: 48px; background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuBJKx30tp4nUkgLr-R3-DgDlG6yG_UxqwiKJXaMwo_YSZxiA84isyIYf0XJv9LiwqSc_Yjq9-TW64daOBfU748j773_BTDFi0XQL1rFeGlimC7EPQkMws7qPHmOA3GHFSP6pLQurvnJjDjCn21rb9rNf0rIG8xIwtyRYZPWUQO8jQt35tzCckn6yjrnSaWWIm9DfXlauwb9YrXMc7Mx2U0V7L7CDg0wgf83J7FhFxwK5Tt0aaKKvKTZeHKj7r2VXt7IcHYNPL3Xj3o"); background-size: cover; background-position: center;'></div>
                    <div>
                      <p class="fw-bold mb-0">Mariana Costa</p>
                      <p class="small text-muted mb-0">Diretora de Marketing, Soluções Criativas</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-lg-4 col-md-6">
              <div class="card h-100 border-secondary border-opacity-25">
                <div class="card-body p-4 d-flex flex-column">
                  <div class="mb-3 text-warning">
                    <span class="material-symbols-outlined">star</span>
                    <span class="material-symbols-outlined">star</span>
                    <span class="material-symbols-outlined">star</span>
                    <span class="material-symbols-outlined">star</span>
                    <span class="material-symbols-outlined">star</span>
                  </div>
                  <p class="text-muted fst-italic flex-grow-1">"Desde a concepção até o lançamento, o processo foi transparente e colaborativo. O sistema financeiro que eles desenvolveram otimizou nossas operações."</p>
                  <div class="d-flex align-items-center gap-3 mt-3">
                    <div class="rounded-circle" style='width: 48px; height: 48px; background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuBMcLu-bnelZFNJyRrFhvefYmR3YFdJu8VHx5JNHln4KWlWeE8QA1rg0JN4Q5oyTwcy6tdk_ZJ-F1p6wnnodmg3FGhDOQYBwcqqMdJV8pq3rHf1HKqTchLnSfwh7VgJlKE-RYbg9aCiOLpiwlPWhkCZYDNKTowxkCmgVCAdT8U6b3pr1g2Ye2pT1UJzDv7YW6kBDqdoNpTXXNoWmpK4TsaMuBdpGcn_ZKl6JxTkOIQFewzwvbTrwuPePiTrbUoP0ln2CllqmXuFtWo"); background-size: cover; background-position: center;'></div>
                    <div>
                      <p class="fw-bold mb-0">Ricardo Almeida</p>
                      <p class="small text-muted mb-0">CFO, Gestão Eficiente</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Process Section -->
      <section class="py-5 bg-light">
        <div class="container" style="max-width: 1200px;">
          <div class="text-center mb-5">
            <h2 class="display-5 fw-bold mb-3">Nosso Processo Simplificado</h2>
            <p class="lead text-muted">Da ideia ao lançamento, seguimos um processo claro para garantir o sucesso do seu projeto.</p>
          </div>
          <div class="row g-4 text-center">
            <div class="col-lg-3 col-md-6">
              <div class="d-flex flex-column align-items-center">
                <div class="rounded-circle d-flex align-items-center justify-content-center mb-3" style="width: 48px; height: 48px; background-color: rgba(74, 111, 165, 0.2); color: #4A6FA5;">
                  <span class="material-symbols-outlined">lightbulb</span>
                </div>
                <h3 class="h5 fw-bold mb-2">1. Descoberta</h3>
                <p class="small text-muted">Analisamos suas necessidades e definimos os objetivos.</p>
              </div>
            </div>
            <div class="col-lg-3 col-md-6">
              <div class="d-flex flex-column align-items-center">
                <div class="rounded-circle d-flex align-items-center justify-content-center mb-3" style="width: 48px; height: 48px; background-color: rgba(74, 111, 165, 0.2); color: #4A6FA5;">
                  <span class="material-symbols-outlined">design_services</span>
                </div>
                <h3 class="h5 fw-bold mb-2">2. Design</h3>
                <p class="small text-muted">Criamos a arquitetura e o design da interface do usuário.</p>
              </div>
            </div>
            <div class="col-lg-3 col-md-6">
              <div class="d-flex flex-column align-items-center">
                <div class="rounded-circle d-flex align-items-center justify-content-center mb-3" style="width: 48px; height: 48px; background-color: rgba(74, 111, 165, 0.2); color: #4A6FA5;">
                  <span class="material-symbols-outlined">code</span>
                </div>
                <h3 class="h5 fw-bold mb-2">3. Desenvolvimento</h3>
                <p class="small text-muted">Codificamos a solução com tecnologia de ponta.</p>
              </div>
            </div>
            <div class="col-lg-3 col-md-6">
              <div class="d-flex flex-column align-items-center">
                <div class="rounded-circle d-flex align-items-center justify-content-center mb-3" style="width: 48px; height: 48px; background-color: rgba(74, 111, 165, 0.2); color: #4A6FA5;">
                  <span class="material-symbols-outlined">rocket_launch</span>
                </div>
                <h3 class="h5 fw-bold mb-2">4. Lançamento</h3>
                <p class="small text-muted">Implementamos o projeto e oferecemos suporte contínuo.</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Contact Section -->
      <section id="contato" class="py-5">
        <div class="container" style="max-width: 960px;">
          <div class="text-center mb-5">
            <h2 class="display-5 fw-bold mb-3">Vamos construir algo incrível juntos?</h2>
            <p class="lead text-muted">Entre em contato para uma consulta gratuita e descubra como podemos ajudar seu negócio a crescer.</p>
          </div>
          <form class="row g-3" @submit="submitForm">
            <!-- Success Message -->
            <div v-if="formStatus.success" class="col-12">
              <div class="alert alert-success d-flex align-items-center" role="alert">
                <span class="material-symbols-outlined me-2">check_circle</span>
                <div>{{ formStatus.message }}</div>
              </div>
            </div>
            
            <!-- Error Message -->
            <div v-if="formStatus.error" class="col-12">
              <div class="alert alert-danger d-flex align-items-center" role="alert">
                <span class="material-symbols-outlined me-2">error</span>
                <div>{{ formStatus.message }}</div>
              </div>
            </div>

            <div class="col-md-6">
              <label for="nome" class="form-label fw-medium">Nome <span class="text-danger">*</span></label>
              <input 
                type="text" 
                class="form-control" 
                id="nome" 
                v-model="formData.nome"
                autocomplete="given-name"
                required
              >
            </div>
            <div class="col-md-6">
              <label for="empresa" class="form-label fw-medium">Empresa</label>
              <input 
                type="text" 
                class="form-control" 
                id="empresa" 
                v-model="formData.empresa"
                autocomplete="organization"
              >
            </div>
            <div class="col-12">
              <label for="email" class="form-label fw-medium">Email <span class="text-danger">*</span></label>
              <input 
                type="email" 
                class="form-control" 
                id="email" 
                v-model="formData.email"
                autocomplete="email"
                required
              >
            </div>
            <div class="col-12">
              <label for="telefone" class="form-label fw-medium">
                <span class="material-symbols-outlined align-middle me-1" style="font-size: 18px; color: #25D366;">chat</span>
                WhatsApp <span class="text-danger">*</span>
              </label>
              <input 
                type="tel" 
                class="form-control" 
                id="telefone" 
                v-model="formData.telefone"
                @input="formatPhone"
                placeholder="(11) 99999-9999"
                autocomplete="tel"
                required
              >
              <small class="text-muted">Formato: (XX) XXXXX-XXXX</small>
            </div>
            <div class="col-12">
              <label for="mensagem" class="form-label fw-medium">Mensagem <span class="text-danger">*</span></label>
              <textarea 
                class="form-control" 
                id="mensagem" 
                v-model="formData.mensagem"
                rows="4"
                required
              ></textarea>
            </div>
            <div class="col-12 text-center">
              <button 
                type="submit" 
                class="btn btn-lg text-white px-5" 
                style="background-color: #008B8B;"
                :disabled="formStatus.loading"
              >
                <span v-if="!formStatus.loading">Enviar Mensagem</span>
                <span v-else>
                  <span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
                  Enviando...
                </span>
              </button>
            </div>
          </form>
        </div>
      </section>
    </main>

    <!-- Footer -->
    <footer class="text-white py-5" style="background-color: #0052CC;">
      <div class="container" style="max-width: 1200px;">
        <div class="row">
          <div class="col-lg-4">
            <div class="d-flex align-items-center gap-2 mb-3">
              <img src="/src/views/Logotipo.png" alt="Roldan Eng Software Logo" style="width: 36px; height: 36px; object-fit: contain; filter: brightness(0) invert(1);">
              <h2 class="mb-0 fw-bold fs-5">Roldan Eng Software</h2>
            </div>
            <p class="small text-white-50 mb-3">Soluções de software personalizadas para impulsionar o crescimento do seu negócio.</p>
            <div class="d-flex gap-3">
              <a href="#" class="text-white-50">
                <svg class="bi" width="24" height="24" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z" clip-rule="evenodd"></path></svg>
              </a>
            </div>
          </div>
        </div>
        <div class="border-top border-white border-opacity-25 mt-4 pt-4">
          <p class="small text-white-50 mb-0">© 2025 Roldan Eng Software. Todos os direitos reservados.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'LandingPage',
  data() {
    return {
      formData: {
        nome: '',
        empresa: '',
        email: '',
        telefone: '',
        mensagem: ''
      },
      formStatus: {
        loading: false,
        success: false,
        error: false,
        message: ''
      }
    }
  },
  methods: {
    async submitForm(event) {
      event.preventDefault()
      
      // Validação básica
      if (!this.formData.nome || !this.formData.email || !this.formData.telefone || !this.formData.mensagem) {
        this.formStatus.error = true
        this.formStatus.message = 'Por favor, preencha todos os campos obrigatórios.'
        setTimeout(() => {
          this.formStatus.error = false
          this.formStatus.message = ''
        }, 3000)
        return
      }

      // Validação de email
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      if (!emailRegex.test(this.formData.email)) {
        this.formStatus.error = true
        this.formStatus.message = 'Por favor, insira um email válido.'
        setTimeout(() => {
          this.formStatus.error = false
          this.formStatus.message = ''
        }, 3000)
        return
      }

      // Validação de telefone
      const phoneRegex = /^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$/
      if (!phoneRegex.test(this.formData.telefone.replace(/\s/g, ''))) {
        this.formStatus.error = true
        this.formStatus.message = 'Por favor, insira um telefone válido (ex: (11) 99999-9999).'
        setTimeout(() => {
          this.formStatus.error = false
          this.formStatus.message = ''
        }, 3000)
        return
      }

      this.formStatus.loading = true
      this.formStatus.error = false
      this.formStatus.success = false

      try {
        // Aqui você pode adicionar a chamada para o backend
        // Por enquanto, vamos simular o envio
        await new Promise(resolve => setTimeout(resolve, 1500))
        
        // Simulação de sucesso
        this.formStatus.success = true
        this.formStatus.message = 'Mensagem enviada com sucesso! Entraremos em contato em breve.'
        
        // Limpar formulário
        this.formData = {
          nome: '',
          empresa: '',
          email: '',
          telefone: '',
          mensagem: ''
        }

        // Remover mensagem de sucesso após 5 segundos
        setTimeout(() => {
          this.formStatus.success = false
          this.formStatus.message = ''
        }, 5000)
      } catch (error) {
        this.formStatus.error = true
        this.formStatus.message = 'Erro ao enviar mensagem. Por favor, tente novamente.'
        setTimeout(() => {
          this.formStatus.error = false
          this.formStatus.message = ''
        }, 3000)
      } finally {
        this.formStatus.loading = false
      }
    },
    formatPhone() {
      // Remove tudo que não é número
      let phone = this.formData.telefone.replace(/\D/g, '')
      
      // Limita a 11 dígitos
      phone = phone.substring(0, 11)
      
      // Formata o telefone
      if (phone.length > 10) {
        // Formato: (XX) XXXXX-XXXX
        phone = phone.replace(/(\d{2})(\d{5})(\d{4})/, '($1) $2-$3')
      } else if (phone.length > 6) {
        // Formato: (XX) XXXX-XXXX
        phone = phone.replace(/(\d{2})(\d{4})(\d{0,4})/, '($1) $2-$3')
      } else if (phone.length > 2) {
        // Formato: (XX) XXXX
        phone = phone.replace(/(\d{2})(\d{0,5})/, '($1) $2')
      } else if (phone.length > 0) {
        // Formato: (XX
        phone = phone.replace(/(\d*)/, '($1')
      }
      
      this.formData.telefone = phone
    }
  }
}
</script>

<style scoped>
.material-symbols-outlined {
  font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
}

/* Smooth scroll */
html {
  scroll-behavior: smooth;
}

/* Offset para compensar navbar fixo - usando padding ao invés de margin */
section[id]::before {
  content: '';
  display: block;
  height: 80px;
  margin-top: -80px;
  visibility: hidden;
}
</style>
