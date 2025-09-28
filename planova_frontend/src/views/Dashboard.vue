<template>
  <div class="dashboard">

    <!-- Butoane Add elegante -->
    <div class="header-actions">
      <button @click="showAddPopup('task')" class="btn btn-primary">
        <span class="icon">➕</span> Adaugă Task
      </button>
      <button @click="showAddPopup('event')" class="btn btn-secondary">
        <span class="icon">📅</span> Adaugă Eveniment
      </button>
      <button @click="showArchive()" class="btn btn-archive" v-if="archive.length">
        <span class="icon">🗄️</span> Vezi Arhiva ({{ archive.length }})
      </button>
    </div>

    <!-- Dashboard cu coloane -->
    <div class="dashboard-grid">
      <div
        class="column"
        v-for="(col, colIndex) in columns"
        :key="colIndex"
        @dragover.prevent="onDragOver($event)"
        @dragleave="onDragLeave($event)"
        @drop="onDrop($event, colIndex)"
      >
        <h3>{{ titles[colIndex] }} <span class="count">({{ col.length }})</span></h3>

        <!-- Empty state -->
        <div v-if="col.length === 0" class="empty-column">
          <p>{{ getEmptyMessage(colIndex) }}</p>
        </div>

        <!-- Cards -->
        <div
          v-for="(item, index) in col"
          :key="item.id"
          class="card"
          :class="[{ done: colIndex === 2 }, item.type]"
          draggable="true"
          @dragstart="onDragStart($event, colIndex, index)"
        >
          <div class="card-header">
            <div class="card-content">
              <div class="card-title">{{ item.title }}</div>
              <div class="card-event">{{ item.event }}</div>
              <div class="card-date" v-if="item.date">
                <span class="icon">📅</span> {{ formatDate(item.date) }}
              </div>
            </div>
            <span class="card-type">{{ item.type === 'task' ? '📋' : '📅' }}</span>
          </div>

          <div class="card-comments" v-if="item.comments">
            <span class="icon">💬</span> {{ item.comments }}
          </div>

          <div class="card-actions">
            <button 
              v-if="isMobile && colIndex !== 2" 
              @click="showMovePopup(colIndex, index)"
              class="card-btn btn-move">
              ↔️
            </button>
            
            <button 
              @click="showDetails(item)" 
              class="card-btn btn-details">
              👁️
            </button>
            
            <button 
              @click="archiveItem(colIndex, index)" 
              class="card-btn btn-archive">
              🗄️
            </button>
            
            <button 
              v-if="colIndex === 2" 
              @click="deleteTask(colIndex, index)" 
              class="card-btn btn-delete">
              🗑️
            </button>
            
            <button 
              v-if="colIndex === 2" 
              @click="moveCard(colIndex, index, 0)" 
              class="card-btn btn-restore">
              ↩️
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Popup Add Item -->
    <div v-if="popup.visible" class="popup-overlay" @click.self="closeAddPopup">
      <div class="popup">
        <div class="popup-header">
          <h4>✨ Adaugă {{ popup.type === 'task' ? 'Task Nou' : 'Eveniment Nou' }}</h4>
          <button @click="closeAddPopup" class="close-btn">✕</button>
        </div>
        
        <div class="form-group">
          <label class="form-label">Titlu *</label>
          <input 
            v-model="popup.title" 
            placeholder="Introdu titlul..." 
            class="form-input"
            @keyup.enter="addItem">
        </div>

        <div class="form-group">
          <label class="form-label">Descriere / Eveniment *</label>
          <input 
            v-model="popup.event" 
            placeholder="Descrierea task-ului sau evenimentului..." 
            class="form-input">
        </div>

        <div class="form-group">
          <label class="form-label">Data (opțional)</label>
          <input 
            v-model="popup.date" 
            type="date" 
            class="form-input">
        </div>

        <div class="form-group">
          <label class="form-label">Comentarii (opțional)</label>
          <textarea 
            v-model="popup.comments" 
            placeholder="Detalii suplimentare, note..." 
            class="form-textarea">
          </textarea>
        </div>

        <div class="popup-actions">
          <button @click="addItem" class="btn btn-primary">
            ✅ Adaugă {{ popup.type === 'task' ? 'Task' : 'Eveniment' }}
          </button>
          <button @click="closeAddPopup" class="btn btn-cancel">
            ❌ Anulează
          </button>
        </div>
      </div>
    </div>

    <!-- Popup Move (Mobile) -->
    <div v-if="movePopup.visible" class="popup-overlay" @click.self="closeMovePopup">
      <div class="popup">
        <div class="popup-header">
          <h4>📱 Mută Cardul</h4>
          <button @click="closeMovePopup" class="close-btn">✕</button>
        </div>
        
        <p class="popup-subtitle">Selectează coloana de destinație:</p>
        
        <div class="move-options">
          <button
            v-for="(title, idx) in titles"
            :key="idx"
            :disabled="idx === movePopup.fromCol"
            @click="moveCard(movePopup.fromCol, movePopup.index, idx)"
            class="btn move-btn"
            :class="idx === movePopup.fromCol ? 'btn-disabled' : 'btn-primary'">
            {{ title }}
          </button>
        </div>
      </div>
    </div>

    <!-- Popup Archive -->
    <div v-if="archivePopup.visible" class="popup-overlay" @click.self="closeArchivePopup">
      <div class="popup popup-large">
        <div class="popup-header">
          <h4>🗄️ Arhiva</h4>
          <button @click="closeArchivePopup" class="close-btn">✕</button>
        </div>
        
        <div class="archive-stats">
          📊 Total elemente arhivate: <strong>{{ archive.length }}</strong>
          <br>
          👀 Se afișează primele 20 de elemente
        </div>

        <div class="archive-list">
          <div
            v-for="(item, i) in archive.slice(0, 20)"
            :key="item.id"
            class="card archived-card"
            :class="item.type">
            
            <div class="card-header">
              <div class="card-content">
                <div class="card-title">{{ item.title }}</div>
                <div class="card-event">{{ item.event }}</div>
                <div class="card-date" v-if="item.date">
                  📅 {{ formatDate(item.date) }}
                </div>
              </div>
              <span class="card-type">{{ item.type === 'task' ? '📋' : '📅' }}</span>
            </div>

            <div class="card-comments" v-if="item.comments">
              💬 {{ item.comments }}
            </div>

            <div class="card-actions">
              <button @click="restoreFromArchive(i)" class="card-btn btn-restore">
                ↩️ Restaurează
              </button>
              <button @click="deleteFromArchive(i)" class="card-btn btn-delete">
                🗑️ Șterge
              </button>
            </div>
          </div>

          <div v-if="archive.length === 0" class="empty-archive">
            <p>Niciun element în arhivă</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Popup Details -->
    <div v-if="detailsPopup.visible" class="popup-overlay" @click.self="closeDetailsPopup">
      <div class="popup">
        <div class="popup-header">
          <h4>📋 Detalii {{ detailsPopup.item?.type === 'task' ? 'Task' : 'Eveniment' }}</h4>
          <button @click="closeDetailsPopup" class="close-btn">✕</button>
        </div>
        
        <div v-if="detailsPopup.item" class="details-content">
          <div class="detail-group">
            <label class="detail-label">Titlu</label>
            <div class="detail-value">{{ detailsPopup.item.title }}</div>
          </div>

          <div class="detail-group">
            <label class="detail-label">Descriere</label>
            <div class="detail-value">{{ detailsPopup.item.event }}</div>
          </div>

          <div class="detail-group" v-if="detailsPopup.item.date">
            <label class="detail-label">Data</label>
            <div class="detail-value">📅 {{ formatDate(detailsPopup.item.date) }}</div>
          </div>

          <div class="detail-group" v-if="detailsPopup.item.comments">
            <label class="detail-label">Comentarii</label>
            <div class="detail-value">{{ detailsPopup.item.comments }}</div>
          </div>

          <div class="detail-group">
            <label class="detail-label">Tip</label>
            <div class="detail-value">{{ detailsPopup.item.type === 'task' ? '📋 Task' : '📅 Eveniment' }}</div>
          </div>
        </div>

        <div class="popup-actions">
          <button @click="generateContract(detailsPopup.item)" class="btn btn-primary">
            📄 Generează Contract
          </button>
          <button @click="generatePDF(detailsPopup.item)" class="btn btn-secondary">
            📁 Exportă PDF
          </button>
          <button @click="closeDetailsPopup" class="btn btn-cancel">
            ❌ Închide
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { reactive, ref, onMounted } from "vue"

export default {
  setup() {
    const titles = ["To Do", "In Progress", "Done"]
    
    const columns = reactive([
      [
        {
          id: 1,
          title: "Finalizare proiect website",
          event: "Trebuie să termin designul și implementarea",
          date: "2025-01-01",
          comments: "Urgent! Deadline la sfârșitul săptămânii",
          type: "task"
        }
      ],
      [
        {
          id: 2,
          title: "Meeting cu clientul",
          event: "Discuții despre cerințele noi",
          date: "2024-12-28",
          comments: "Să pregătesc prezentarea",
          type: "event"
        }
      ],
      []
    ])
    
    const archive = reactive([])
    const generalComment = ref('')
    const isMobile = ref(false)

    // Popup states
    const popup = reactive({
      visible: false,
      type: "task",
      title: "",
      event: "",
      date: "",
      comments: ""
    })

    const movePopup = reactive({
      visible: false,
      fromCol: null,
      index: null
    })

    const archivePopup = reactive({
      visible: false
    })

    const detailsPopup = reactive({
      visible: false,
      item: null
    })

    // Drag & Drop
    let draggedItem = null
    let draggedFromCol = null
    let draggedIndex = null

    onMounted(() => {
      checkMobile()
      window.addEventListener("resize", checkMobile)
    })

    function checkMobile() {
      isMobile.value = window.innerWidth <= 768
    }

    function onDragStart(event, colIndex, itemIndex) {
      if (isMobile.value) return
      draggedItem = columns[colIndex][itemIndex]
      draggedFromCol = colIndex
      draggedIndex = itemIndex
    }

    function onDragOver(event) {
      if (!isMobile.value) {
        event.currentTarget.classList.add("drag-over")
      }
    }

    function onDragLeave(event) {
      if (!isMobile.value) {
        event.currentTarget.classList.remove("drag-over")
      }
    }

    function onDrop(event, colIndex) {
      if (!isMobile.value && draggedItem) {
        columns[draggedFromCol].splice(draggedIndex, 1)
        columns[colIndex].push(draggedItem)
      }
      if (!isMobile.value) {
        event.currentTarget.classList.remove("drag-over")
      }
      draggedItem = null
      draggedFromCol = null
      draggedIndex = null
    }

    function showAddPopup(type) {
      popup.visible = true
      popup.type = type
      popup.title = ""
      popup.event = ""
      popup.date = ""
      popup.comments = ""
    }

    function closeAddPopup() {
      popup.visible = false
    }

    function addItem() {
      if (!popup.title.trim() || !popup.event.trim()) {
        alert("Te rog completează cel puțin titlul și descrierea!")
        return
      }

      const newId = Math.max(
        0,
        ...columns.flat().map(c => c.id),
        ...archive.map(a => a.id)
      ) + 1

      columns[0].push({
        id: newId,
        title: popup.title.trim(),
        event: popup.event.trim(),
        date: popup.date,
        comments: popup.comments.trim(),
        type: popup.type
      })

      popup.visible = false
    }

    function showMovePopup(fromCol, index) {
      movePopup.visible = true
      movePopup.fromCol = fromCol
      movePopup.index = index
    }

    function closeMovePopup() {
      movePopup.visible = false
    }

    function moveCard(fromCol, index, toCol) {
      if (fromCol === toCol) {
        movePopup.visible = false
        return
      }
      const card = columns[fromCol][index]
      columns[fromCol].splice(index, 1)
      columns[toCol].push(card)
      movePopup.visible = false
    }

    function deleteTask(colIndex, index) {
      if (confirm("Ești sigur că vrei să ștergi definitiv acest item?")) {
        columns[colIndex].splice(index, 1)
      }
    }

    function archiveItem(colIndex, index) {
      const card = columns[colIndex][index]
      columns[colIndex].splice(index, 1)
      archive.push(card)
    }

    function showArchive() {
      archivePopup.visible = true
    }

    function closeArchivePopup() {
      archivePopup.visible = false
    }

    function restoreFromArchive(index) {
      const card = archive[index]
      archive.splice(index, 1)
      columns[0].push(card)
    }

    function deleteFromArchive(index) {
      if (confirm("Ștergi definitiv acest item din arhivă?")) {
        archive.splice(index, 1)
      }
    }

    function showDetails(item) {
      detailsPopup.visible = true
      detailsPopup.item = item
    }

    function closeDetailsPopup() {
      detailsPopup.visible = false
    }

    function generateContract(item) {
      alert(`📄 Contract generat pentru: "${item.title}"\n\nAcesta ar fi un contract sau document oficial bazat pe detaliile task-ului. În implementarea reală, aici ar fi logica de generare a contractului.`)
      detailsPopup.visible = false
    }

    function generatePDF(item) {
      alert(`📁 PDF exportat pentru: "${item.title}"\n\nFișierul ar fi descărcat automat. În implementarea reală, aici ar fi logica de generare și download a PDF-ului.`)
      detailsPopup.visible = false
    }

    function formatDate(dateString) {
      if (!dateString) return ''
      const date = new Date(dateString)
      return date.toLocaleDateString('ro-RO', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      })
    }

    function getEmptyMessage(colIndex) {
      const messages = [
        'Niciun task de făcut',
        'Niciun task în progres',
        'Niciun task finalizat'
      ]
      return messages[colIndex] || ''
    }

    return {
      titles,
      columns,
      archive,
      generalComment,
      isMobile,
      popup,
      movePopup,
      archivePopup,
      detailsPopup,
      onDragStart,
      onDragOver,
      onDragLeave,
      onDrop,
      showAddPopup,
      closeAddPopup,
      addItem,
      showMovePopup,
      closeMovePopup,
      moveCard,
      deleteTask,
      archiveItem,
      showArchive,
      closeArchivePopup,
      restoreFromArchive,
      deleteFromArchive,
      showDetails,
      closeDetailsPopup,
      generateContract,
      generatePDF,
      formatDate,
      getEmptyMessage
    }
  }
}
</script>

<style scoped>
@import '../assets/css/dashboard_enhanced.css';
</style>